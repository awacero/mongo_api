"""Flask application factory serving sensor data from MongoDB."""

from flask import Flask, jsonify
from pymongo import errors
import logging


logger = logging.getLogger(__name__)


def create_app(mongo_collection):
    """Create and return the Flask application.

    Parameters
    ----------
    mongo_collection : pymongo.collection.Collection
        Collection object used to query sensor data.

    Returns
    -------
    Flask
        Configured Flask application exposing the API endpoints.
    """
    app = Flask(__name__)

    @app.route("/api/sensor-data", methods=["GET"])
    def get_sensor_data():
        """Return the latest sensor data records as JSON."""
        logger.debug("Handling /api/sensor-data request")
        try:
            cursor = mongo_collection.find().sort("timestamp", -1).limit(100)
            result = []
            for doc in cursor:
                result.append(
                    {
                        "timestamp": doc.get("timestamp"),
                        "temperature": doc.get("temperature"),
                        "humidity": doc.get("humidity"),
                    }
                )
            logger.debug("Returning %d sensor records", len(result))
            return jsonify(result)
        except errors.PyMongoError as exc:
            logger.error("Database error: %s", exc)
            return jsonify({"error": "Database error"}), 500

    return app
