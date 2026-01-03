from flask import Flask, jsonify

from routes.users import users_bp
from routes.cars import cars_bp
from routes.rentals import rentals_bp
from routes.delinquency import delinq_bp

app = Flask(__name__)


app.register_blueprint(users_bp)
app.register_blueprint(cars_bp)
app.register_blueprint(rentals_bp)
app.register_blueprint(delinq_bp)

@app.get("/")
def home():
    return jsonify({"status": "ok", "message": "Lyfter Car Rental API running"})

if __name__ == "__main__":
    app.run(debug=True)

