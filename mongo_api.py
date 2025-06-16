from flask import Flask, jsonify
from pymongo import MongoClient, errors
from datetime import datetime

app = Flask(__name__)
#client = MongoClient("mongodb://192.168.1.90:27017")  # Change as needed
try:
    client = MongoClient(
        "mongodb://grafana_user:mi_clave_segura@192.168.132.10:27017/test_db?authSource=test_db"
    )
except errors.PyMongoError as exc:
    raise SystemExit(f"Mongo connection failed: {exc}")

db = client["test_db"]
collection = db["sensor_data"]

@app.route("/api/sensor-data", methods=["GET"])
def get_sensor_data():
    try:
        cursor = collection.find().sort("timestamp", -1).limit(100)
        result = []
        for doc in cursor:
            result.append({
                "timestamp": doc.get("timestamp"),
                "temperature": doc.get("temperature"),
                "humidity": doc.get("humidity")
            })
        return jsonify(result)
    except errors.PyMongoError:
        return jsonify({"error": "Database error"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


