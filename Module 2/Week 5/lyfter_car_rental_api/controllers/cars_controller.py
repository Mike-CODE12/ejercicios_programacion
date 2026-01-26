from utils.http import ok, error


class CarsController:
    def __init__(self, cars_repo):
        self.cars_repo = cars_repo

    def create_car(self, data: dict):
        required = ["make", "model", "manufacturing_year", "car_condition"]
        missing = [k for k in required if k not in data]
        if missing:
            return error(f"Missing fields: {missing}", 400)

        row = self.cars_repo.create_car(
            data["make"],
            data["model"],
            data["manufacturing_year"],
            data["car_condition"],
        )
        return ok(row, 201)

    def list_cars(self, filters: dict):
        rows = self.cars_repo.list_cars(filters)
        return ok(rows)

    def change_car_status(self, car_id: int, data: dict):
        if "car_condition" not in data:
            return error("Expected car_condition", 400)

        row = self.cars_repo.update_car_condition(car_id, data["car_condition"])
        if not row:
            return error("Car not found", 404)

        return ok(row)
