class UsersRepository:
    def __init__(self, db):
        self.db = db

    def create_user(self, name: str, email: str, phone_number: str):
        return self.db.execute_returning(
            """
            INSERT INTO users (name, email, phone_number)
            VALUES (%s, %s, %s)
            RETURNING *;
            """,
            (name, email, phone_number),
        )

    def list_users(self, filters: dict):
        allowed = {"id", "name", "email", "phone_number", "user_status", "is_overdue"}

        where = []
        values = []

        for k, v in filters.items():
            if k in allowed:
                where.append(f"{k} = %s")
                values.append(v)

        sql = "SELECT * FROM users"
        if where:
            sql += " WHERE " + " AND ".join(where)
        sql += " ORDER BY id;"

        return self.db.fetch_all(sql, tuple(values))

    def update_user_status(self, user_id: int, user_status: str):
        return self.db.execute_returning(
            "UPDATE users SET user_status = %s WHERE id = %s RETURNING *;",
            (user_status, user_id),
        )

    def set_overdue(self, user_id: int, is_overdue: bool):
        return self.db.execute_returning(
            "UPDATE users SET is_overdue = %s WHERE id = %s RETURNING *;",
            (is_overdue, user_id),
        )

    def user_exists(self, user_id: int) -> bool:
        row = self.db.fetch_one("SELECT id FROM users WHERE id = %s;", (user_id,))
        return row is not None
