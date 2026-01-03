from flask import Blueprint, request, jsonify
from db import get_conn

rentals_bp = Blueprint("rentals", __name__)

@rentals_bp.post("/rentals")
def create_rental():
    data = request.get_json(force=True)
    required = ["user_id", "car_id"]
    missing = [k for k in required if k not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {missing}"}), 400

    rental_status = data.get("rental_status", "active")

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            
            cur.execute("SELECT car_condition FROM cars WHERE id = %s;", (data["car_id"],))
            car = cur.fetchone()
            if not car:
                conn.rollback()
                return jsonify({"error": "Car not found"}), 404
            if car["car_condition"] != "available":
                conn.rollback()
                return jsonify({"error": "Car is not available"}), 400

            
            cur.execute(
                """
                INSERT INTO rentals (user_id, car_id, rental_status)
                VALUES (%s, %s, %s)
                RETURNING *;
                """,
                (data["user_id"], data["car_id"], rental_status)
            )
            rental = cur.fetchone()

            
            cur.execute("UPDATE cars SET car_condition = 'rented' WHERE id = %s;", (data["car_id"],))

            conn.commit()
            return jsonify(rental), 201
    finally:
        conn.close()

@rentals_bp.get("/rentals")
def list_rentals():
    filters = request.args.to_dict()
    allowed = {"id","user_id","car_id","rental_date","rental_status"}

    where = []
    values = []

    for k, v in filters.items():
        if k in allowed:
            where.append(f"{k} = %s")
            values.append(v)

    sql = "SELECT * FROM rentals"
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

@rentals_bp.patch("/rentals/<int:rental_id>/status")
def change_rental_status(rental_id):
    data = request.get_json(force=True)
    if "rental_status" not in data:
        return jsonify({"error": "Expected rental_status"}), 400

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE rentals SET rental_status = %s WHERE id = %s RETURNING *;",
                (data["rental_status"], rental_id)
            )
            row = cur.fetchone()
            if not row:
                conn.rollback()
                return jsonify({"error": "Rental not found"}), 404
            conn.commit()
            return jsonify(row)
    finally:
        conn.close()

@rentals_bp.post("/rentals/<int:rental_id>/complete")
def complete_rental(rental_id):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM rentals WHERE id = %s;", (rental_id,))
            rental = cur.fetchone()
            if not rental:
                conn.rollback()
                return jsonify({"error": "Rental not found"}), 404

            
            cur.execute(
                "UPDATE rentals SET rental_status = 'completed' WHERE id = %s RETURNING *;",
                (rental_id,)
            )
            updated = cur.fetchone()

            
            cur.execute("UPDATE cars SET car_condition = 'available' WHERE id = %s;", (rental["car_id"],))

            conn.commit()
            return jsonify(updated)
    finally:
        conn.close()
