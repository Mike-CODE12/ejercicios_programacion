from flask import Flask, jsonify

from db import PgManager

from repositories.users_repository import UsersRepository
from repositories.cars_repository import CarsRepository
from repositories.rentals_repository import RentalsRepository

from controllers.users_controller import UsersController
from controllers.cars_controller import CarsController
from controllers.rentals_controller import RentalsController

from routes.users_routes import build_users_routes
from routes.cars_routes import build_cars_routes
from routes.rentals_routes import build_rentals_routes


DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "postgres",
    "user": "postgres",
    "password": "Funciona",
}

SCHEMA = "lyfter_car_rental"


def create_app():
    app = Flask(__name__)

    db = PgManager(DB_CONFIG, SCHEMA)

    users_repo = UsersRepository(db)
    cars_repo = CarsRepository(db)
    rentals_repo = RentalsRepository(db)

    users_controller = UsersController(users_repo)
    cars_controller = CarsController(cars_repo)
    rentals_controller = RentalsController(rentals_repo)

    app.register_blueprint(build_users_routes(users_controller))
    app.register_blueprint(build_cars_routes(cars_controller))
    app.register_blueprint(build_rentals_routes(rentals_controller))

    @app.get("/")
    def home():
        return jsonify({"status": "ok", "message": "Lyfter Car Rental API running"})

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
