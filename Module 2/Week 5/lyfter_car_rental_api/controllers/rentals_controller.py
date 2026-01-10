from utils.http import ok, error


class RentalsController:
    def __init__(self, rentals_repo):
        self.rentals_repo = rentals_repo

    def create_rental(self, data: dict):
        required = ["user_id", "car_id"]
        missing = [k for k in required if k not in data]
        if missing:
            return error(f"Missing fields: {missing}", 400)

        rental_status = data.get("rental_status", "active")
        result = self.rentals_repo.create_rental_transaction(
            user_id=data["user_id"],
            car_id=data["car_id"],
            rental_status=rental_status,
        )

        if result is None:
            return error("Unexpected error", 500)

        if "error" in result:
            return error(result["error"], result["_status"])

        return ok(result["rental"], 201)

    def list_rentals(self, filters: dict):
        rows = self.rentals_repo.list_rentals(filters)
        return ok(rows)

    def change_rental_status(self, rental_id: int, data: dict):
        if "rental_status" not in data:
            return error("Expected rental_status", 400)

        row = self.rentals_repo.update_rental_status(rental_id, data["rental_status"])
        if not row:
            return error("Rental not found", 404)

        return ok(row)

    def complete_rental(self, rental_id: int):
        result = self.rentals_repo.complete_rental_transaction(rental_id)

        if result is None:
            return error("Unexpected error", 500)

        if "error" in result:
            return error(result["error"], result["_status"])

        return ok(result["rental"])
