from src import config_loader, db_connection, api_service

def main():
    config = config_loader.load_yaml_config("config/config.yaml")
    mongo_cfg = config_loader.load_json_config(config["mongo"]["config_file"])[config["mongo"]["db_id"]]
    collection = db_connection.get_mongo_client(mongo_cfg)
    app = api_service.create_app(collection)
    app.run(host=config["server"]["host"], port=config["server"]["port"])

if __name__ == "__main__":
    main()



###TODO
# add logs
# add trys
# add documentation 