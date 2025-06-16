from src import config_loader, db_connection, api_service, config_logger
import logging, logging.config



def main():
    try:
        logging.info("Loading configuration")
        config = config_loader.load_yaml_config("config/config.yaml")
        mongo_cfg = config_loader.load_json_config(
            config["mongo"]["config_file"]
        )[config["mongo"]["db_id"]]
        collection = db_connection.get_mongo_client(mongo_cfg)
        app = api_service.create_app(collection)
        logging.info("Initialization complete, starting server")
        app.run(
            host=config["server"]["host"],
            port=config["server"]["port"],
        )
    except Exception as exc:
        logging.exception("Application failed to start: %s", exc)

if __name__ == "__main__":

    logger = config_logger.configure_logging()
    logger.info("Logger configurated")
    main()



###TODO
# add logs
# add trys