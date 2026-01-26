from flask import Blueprint, request


def build_rentals_routes(rentals_controller):
    bp = Blueprint("rentals", __name__)

    @bp.post("/rentals")
    def create_rental():
        data = request.get_json(force=True)
        return rentals_controller.create_rental(data)

    @bp.get("/rentals")
    def list_rentals():
        filters = request.args.to_dict()
        return rentals_controller.list_rentals(filters)

    @bp.patch("/rentals/<int:rental_id>/status")
    def change_rental_status(rental_id: int):
        data = request.get_json(force=True)
        return rentals_controller.change_rental_status(rental_id, data)

    @bp.post("/rentals/<int:rental_id>/complete")
    def complete_rental(rental_id: int):
        return rentals_controller.complete_rental(rental_id)

    return bp
