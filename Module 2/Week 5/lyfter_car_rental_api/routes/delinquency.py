from flask import Blueprint, request, jsonify
from db import get_conn

delinq_bp = Blueprint("delinquency", __name__)

@delinq_bp.post("/users/<int:user_id>/delinquent")
def flag_delinquent(user_id):
    data = request.get_json(silent=True) or {}
    reason = data.get("reason")

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM users WHERE id = %s;", (user_id,))
            if not cur.fetchone():
                conn.rollback()
                return jsonify({"error": "User not found"}), 404

            cur.execute(
                """
                INSERT INTO delinquent_users (user_id, reason)
                VALUES (%s, %s)
                ON CONFLICT (user_id) DO UPDATE SET reason = EXCLUDED.reason
                RETURNING *;
                """,
                (user_id, reason)
            )
            row = cur.fetchone()
            conn.commit()
            return jsonify(row), 201
    finally:
        conn.close()

@delinq_bp.get("/delinquents")
def list_delinquents():
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM delinquent_users ORDER BY flagged_at DESC;")
            rows = cur.fetchall()
            return jsonify(rows)
    finally:
        conn.close()
