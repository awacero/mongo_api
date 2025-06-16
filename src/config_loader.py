import yaml
import json
import logging


logger = logging.getLogger(__name__)

def load_yaml_config(file_path):
    """Load YAML configuration file."""
    logger.debug("Loading YAML config from %s", file_path)
    try:
        with open(file_path, 'r') as f:
            cfg = yaml.safe_load(f)
            logger.debug("YAML config loaded successfully")
            return cfg
    except (OSError, yaml.YAMLError) as exc:
        logger.error("Failed to load YAML config %s: %s", file_path, exc)
        raise RuntimeError(f"Error loading YAML config: {file_path}") from exc

def load_json_config(file_path):
    """Load JSON configuration file."""
    logger.debug("Loading JSON config from %s", file_path)
    try:
        with open(file_path, 'r') as f:
            cfg = json.load(f)
            logger.debug("JSON config loaded successfully")
            return cfg
    except (OSError, json.JSONDecodeError) as exc:
        logger.error("Failed to load JSON config %s: %s", file_path, exc)
        raise RuntimeError(f"Error loading JSON config: {file_path}") from exc
