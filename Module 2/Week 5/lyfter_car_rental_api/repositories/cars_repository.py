class CarsRepository:
    def __init__(self, db):
        self.db = db

    def create_car(self, make: str, model: str, manufacturing_year: int, car_condition: str):
        return self.db.execute_returning(
            """
            INSERT INTO cars (make, model, manufacturing_year, car_condition)
            VALUES (%s, %s, %s, %s)
            RETURNING *;
            """,
            (make, model, manufacturing_year, car_condition),
        )

    def list_cars(self, filters: dict):
        allowed = {"id", "make", "model", "manufacturing_year", "car_condition"}

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

        return self.db.fetch_all(sql, tuple(values))

    def update_car_condition(self, car_id: int, car_condition: str):
        return self.db.execute_returning(
            "UPDATE cars SET car_condition = %s WHERE id = %s RETURNING *;",
            (car_condition, car_id),
        )

    def get_car_condition(self, car_id: int):
        return self.db.fetch_one("SELECT car_condition FROM cars WHERE id = %s;", (car_id,))
