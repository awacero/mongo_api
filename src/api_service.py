from flask import Flask, jsonify
from pymongo import errors

def create_app(mongo_collection):
    app = Flask(__name__)

    @app.route("/api/sensor-data", methods=["GET"])
    def get_sensor_data():
        try:
            cursor = mongo_collection.find().sort("timestamp", -1).limit(100)
            result = []
            for doc in cursor:
                result.append({
                    "timestamp": doc.get("timestamp"),
                    "temperature": doc.get("temperature"),
                    "humidity": doc.get("humidity")
                })
            return jsonify(result)
        except errors.PyMongoError as exc:
            return jsonify({"error": "Database error"}), 500

    return app
