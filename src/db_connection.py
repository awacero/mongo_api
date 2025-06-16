from pymongo import MongoClient, errors

##TODO: Add try, except 
def get_mongo_client(cfg):
    """Return a MongoDB collection based on configuration."""
    try:
        uri = (
            f"mongodb://{cfg['user']}:{cfg['password']}@"
            f"{cfg['host']}:{cfg['port']}/{cfg['db_name']}?authSource={cfg['auth_source']}"
        )
    except KeyError as exc:
        raise ValueError("Invalid Mongo configuration") from exc

    try:
        client = MongoClient(uri)
        return client[cfg['db_name']][cfg['collection']]
    except errors.PyMongoError as exc:
        raise ConnectionError("Could not connect to MongoDB") from exc
