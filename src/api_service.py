from flask import Flask, jsonify

def create_app(mongo_collection):
    app = Flask(__name__)

    @app.route("/api/sensor-data", methods=["GET"])
    def get_sensor_data():
        cursor = mongo_collection.find().sort("timestamp", -1).limit(100)
        result = []
        for doc in cursor:
            result.append({
                "timestamp": doc.get("timestamp"),
                "temperature": doc.get("temperature"),
                "humidity": doc.get("humidity")
            })
        return jsonify(result)

    return app