class RentalsRepository:
    def __init__(self, db):
        self.db = db

    def list_rentals(self, filters: dict):
        allowed = {"id", "user_id", "car_id", "rental_status", "start_date", "end_date"}

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

        return self.db.fetch_all(sql, tuple(values))

    def update_rental_status(self, rental_id: int, rental_status: str):
        return self.db.execute_returning(
            "UPDATE rentals SET rental_status = %s WHERE id = %s RETURNING *;",
            (rental_status, rental_id),
        )

    def create_rental_transaction(self, user_id: int, car_id: int, rental_status: str = "active"):
        """
        Transaction rules (based on your current logic):
        - car must exist and be 'available'
        - create rental
        - set car to 'rented'
        """
        def ops(conn, cur):
            cur.execute("SELECT car_condition FROM cars WHERE id = %s;", (car_id,))
            car = cur.fetchone()
            if not car:
                return {"error": "Car not found", "_status": 404}

            if car["car_condition"] != "available":
                return {"error": "Car is not available", "_status": 400}

            cur.execute(
                """
                INSERT INTO rentals (user_id, car_id, rental_status)
                VALUES (%s, %s, %s)
                RETURNING *;
                """,
                (user_id, car_id, rental_status),
            )
            rental = cur.fetchone()

            cur.execute("UPDATE cars SET car_condition = 'rented' WHERE id = %s;", (car_id,))
            return {"rental": rental}

        return self.db.execute_in_transaction(ops)

    def complete_rental_transaction(self, rental_id: int):
        """
        Minimal "complete rental":
        - rental must exist
        - set rental_status = 'completed'
        - set car_condition = 'available'
        """
        def ops(conn, cur):
            cur.execute("SELECT id, car_id FROM rentals WHERE id = %s;", (rental_id,))
            rental = cur.fetchone()
            if not rental:
                return {"error": "Rental not found", "_status": 404}

            cur.execute(
                "UPDATE rentals SET rental_status = 'completed' WHERE id = %s RETURNING *;",
                (rental_id,),
            )
            updated_rental = cur.fetchone()

            cur.execute(
                "UPDATE cars SET car_condition = 'available' WHERE id = %s;",
                (rental["car_id"],),
            )

            return {"rental": updated_rental}

        return self.db.execute_in_transaction(ops)
