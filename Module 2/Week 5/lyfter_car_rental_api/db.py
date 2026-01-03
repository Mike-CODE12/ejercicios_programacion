import psycopg2
import psycopg2.extras

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "postgres",      
    "user": "postgres",
    "password": "Funciona"    
}

SCHEMA = "lyfter_car_rental"

def get_conn():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(f"SET search_path TO {SCHEMA};")
    cur.close()
    return conn
