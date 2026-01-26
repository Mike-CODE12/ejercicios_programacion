import psycopg2
import psycopg2.extras


class PgManager:
    def __init__(self, db_config: dict, schema: str):
        self._db_config = db_config
        self._schema = schema

    def _get_conn(self):
        conn = psycopg2.connect(**self._db_config)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(f"SET search_path TO {self._schema};")
        cur.close()
        return conn

    def fetch_one(self, sql: str, params: tuple = ()):
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                return cur.fetchone()
        finally:
            conn.close()

    def fetch_all(self, sql: str, params: tuple = ()):
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                return cur.fetchall()
        finally:
            conn.close()

    def execute_returning(self, sql: str, params: tuple = ()):
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                row = cur.fetchone()
                if not row:
                    conn.rollback()
                    return None
                conn.commit()
                return row
        finally:
            conn.close()

    def execute_in_transaction(self, operations_fn):
        """
        Runs multiple operations in a single transaction.
        operations_fn receives (conn, cur) and must return a dict (response payload) or None.
        """
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                result = operations_fn(conn, cur)
                if result is None:
                    conn.rollback()
                    return None
                conn.commit()
                return result
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()
