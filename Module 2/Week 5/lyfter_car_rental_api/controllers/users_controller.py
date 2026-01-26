from utils.http import ok, error


class UsersController:
    def __init__(self, users_repo):
        self.users_repo = users_repo

    def create_user(self, data: dict):
        required = ["name", "email", "phone_number"]
        missing = [k for k in required if k not in data]
        if missing:
            return error(f"Missing fields: {missing}", 400)

        row = self.users_repo.create_user(data["name"], data["email"], data["phone_number"])
        return ok(row, 201)

    def list_users(self, filters: dict):
        rows = self.users_repo.list_users(filters)
        return ok(rows)

    def change_user_status(self, user_id: int, data: dict):
        if "user_status" not in data:
            return error("Expected user_status", 400)

        row = self.users_repo.update_user_status(user_id, data["user_status"])
        if not row:
            return error("User not found", 404)

        return ok(row)

    def set_overdue(self, user_id: int, data: dict):
        if "is_overdue" not in data:
            return error("Expected is_overdue", 400)

        row = self.users_repo.set_overdue(user_id, bool(data["is_overdue"]))
        if not row:
            return error("User not found", 404)

        return ok(row)
