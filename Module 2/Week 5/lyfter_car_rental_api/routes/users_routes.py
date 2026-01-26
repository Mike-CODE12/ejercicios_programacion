from flask import Blueprint, request
from utils.http import error


def build_users_routes(users_controller):
    bp = Blueprint("users", __name__)

    @bp.post("/users")
    def create_user():
        data = request.get_json(force=True)
        return users_controller.create_user(data)

    @bp.get("/users")
    def list_users():
        filters = request.args.to_dict()
        return users_controller.list_users(filters)

    @bp.patch("/users/<int:user_id>/status")
    def change_user_status(user_id: int):
        data = request.get_json(force=True)
        return users_controller.change_user_status(user_id, data)

    # Replaces your delinquency module/table
    @bp.patch("/users/<int:user_id>/overdue")
    def set_overdue(user_id: int):
        data = request.get_json(force=True)
        return users_controller.set_overdue(user_id, data)

    return bp
