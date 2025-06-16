from flask import Flask, jsonify
from pymongo import MongoClient, errors
from datetime import datetime
import logging


logger = logging.getLogger(__name__)

app = Flask(__name__)
#client = MongoClient("mongodb://192.168.1.90:27017")  # Change as needed
try:
    logger.info("Connecting to MongoDB for standalone app")
    client = MongoClient(
        "mongodb://grafana_user:mi_clave_segura@192.168.132.10:27017/test_db?authSource=test_db"
    )
    logger.info("MongoDB connection established")
except errors.PyMongoError as exc:
    logger.exception("Mongo connection failed: %s", exc)
    raise SystemExit(f"Mongo connection failed: {exc}")

db = client["test_db"]
collection = db["sensor_data"]

@app.route("/api/sensor-data", methods=["GET"])
def get_sensor_data():
    logger.debug("Standalone endpoint hit")
    try:
        cursor = collection.find().sort("timestamp", -1).limit(100)
        result = []
        for doc in cursor:
            result.append({
                "timestamp": doc.get("timestamp"),
                "temperature": doc.get("temperature"),
                "humidity": doc.get("humidity")
            })
        logger.debug("Returning %d records", len(result))
        return jsonify(result)
    except errors.PyMongoError as exc:
        logger.error("Database error: %s", exc)
        return jsonify({"error": "Database error"}), 500

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app.run(host="0.0.0.0", port=5000)


