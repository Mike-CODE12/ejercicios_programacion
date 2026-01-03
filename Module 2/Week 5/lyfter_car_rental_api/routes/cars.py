from flask import Blueprint, request, jsonify
from db import get_conn

cars_bp = Blueprint("cars", __name__)

@cars_bp.post("/cars")
def create_car():
    data = request.get_json(force=True)
    required = ["make", "model", "manufacturing_year", "car_condition"]
    missing = [k for k in required if k not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {missing}"}), 400

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO cars (make, model, manufacturing_year, car_condition)
                VALUES (%s, %s, %s, %s)
                RETURNING *;
                """,
                (data["make"], data["model"], data["manufacturing_year"], data["car_condition"])
            )
            row = cur.fetchone()
            conn.commit()
            return jsonify(row), 201
    finally:
        conn.close()

@cars_bp.get("/cars")
def list_cars():
    filters = request.args.to_dict()
    allowed = {"id","make","model","manufacturing_year","car_condition"}

    where = []
    values = []

    for k, v in filters.items():
        if k in allowed:
            where.append(f"{k} = %s")
            values.append(v)

    sql = "SELECT * FROM cars"
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

@cars_bp.patch("/cars/<int:car_id>/status")
def change_car_status(car_id):
    data = request.get_json(force=True)
    if "car_condition" not in data:
        return jsonify({"error": "Expected car_condition"}), 400

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE cars SET car_condition = %s WHERE id = %s RETURNING *;",
                (data["car_condition"], car_id)
            )
            row = cur.fetchone()
            if not row:
                conn.rollback()
                return jsonify({"error": "Car not found"}), 404
            conn.commit()
            return jsonify(row)
    finally:
        conn.close()
