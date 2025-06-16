"""MongoDB connection helper functions."""

from pymongo import MongoClient, errors
import logging


logger = logging.getLogger(__name__)


def get_mongo_client(cfg):
    """Create a MongoDB client based on the provided configuration.

    Parameters
    ----------
    cfg : dict
        Dictionary with connection parameters, such as ``user``, ``password``,
        ``host``, ``port``, ``db_name``, ``collection``, and ``auth_source``.

    Returns
    -------
    pymongo.collection.Collection
        Collection handle for the configured database.
    """
    try:
        uri = (
            f"mongodb://{cfg['user']}:{cfg['password']}@"
            f"{cfg['host']}:{cfg['port']}/{cfg['db_name']}?authSource={cfg['auth_source']}"
        )
    except KeyError as exc:
        logger.error("Invalid Mongo configuration: missing %s", exc)
        raise ValueError("Invalid Mongo configuration") from exc

    try:
        logger.debug("Connecting to MongoDB at %s", uri)
        client = MongoClient(uri)
        logger.info("MongoDB connection established")
        return client[cfg["db_name"]][cfg["collection"]]
    except errors.PyMongoError as exc:
        logger.error("MongoDB connection failed: %s", exc)
        raise ConnectionError("Could not connect to MongoDB") from exc
