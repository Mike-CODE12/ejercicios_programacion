from flask import Blueprint, request


def build_cars_routes(cars_controller):
    bp = Blueprint("cars", __name__)

    @bp.post("/cars")
    def create_car():
        data = request.get_json(force=True)
        return cars_controller.create_car(data)

    @bp.get("/cars")
    def list_cars():
        filters = request.args.to_dict()
        return cars_controller.list_cars(filters)

    @bp.patch("/cars/<int:car_id>/status")
    def change_car_status(car_id: int):
        data = request.get_json(force=True)
        return cars_controller.change_car_status(car_id, data)

    return bp
