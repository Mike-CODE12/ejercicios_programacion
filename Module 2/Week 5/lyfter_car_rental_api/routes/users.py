from flask import Blueprint, request, jsonify
from db import get_conn

users_bp = Blueprint("users", __name__)

@users_bp.post("/users")
def create_user():
    data = request.get_json(force=True)

    required = ["name", "email", "username", "password", "date_of_birth"]
    missing = [k for k in required if k not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {missing}"}), 400

    account_status = data.get("account_status", True)

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO users (name, email, username, password, date_of_birth, account_status)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING *;
                """,
                (data["name"], data["email"], data["username"], data["password"], data["date_of_birth"], account_status)
            )
            row = cur.fetchone()
            conn.commit()
            return jsonify(row), 201
    finally:
        conn.close()

@users_bp.get("/users")
def list_users():

    filters = request.args.to_dict()

    allowed = {"id","name","email","username","password","date_of_birth","account_status"}
    where = []
    values = []

    for k, v in filters.items():
        if k in allowed:
            if v.lower() in ("true", "false"):
                v = v.lower() == "true"
            where.append(f"{k} = %s")
            values.append(v)

    sql = "SELECT * FROM users"
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " ORDER BY id;"

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, values)
            rows = cur.fetchall()
            return jsonify(rows)
    finally:
        conn.close()

@users_bp.patch("/users/<int:user_id>/status")
def change_user_status(user_id):
    data = request.get_json(force=True)
    if "account_status" not in data:
        return jsonify({"error": "Expected account_status"}), 400

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE users SET account_status = %s WHERE id = %s RETURNING *;",
                (bool(data["account_status"]), user_id)
            )
            row = cur.fetchone()
            if not row:
                conn.rollback()
                return jsonify({"error": "User not found"}), 404
            conn.commit()
            return jsonify(row)
    finally:
        conn.close()
