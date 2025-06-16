from pymongo import MongoClient

##TODO: Add try, except 
def get_mongo_client(cfg):
    uri = f"mongodb://{cfg['user']}:{cfg['password']}@{cfg['host']}:{cfg['port']}/{cfg['db_name']}?authSource={cfg['auth_source']}"
    client = MongoClient(uri)
    return client[cfg['db_name']][cfg['collection']]