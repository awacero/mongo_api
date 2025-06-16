import yaml
import json

def load_yaml_config(file_path):
    """Load YAML configuration file."""
    try:
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)
    except (OSError, yaml.YAMLError) as exc:
        raise RuntimeError(f"Error loading YAML config: {file_path}") from exc

def load_json_config(file_path):
    """Load JSON configuration file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Error loading JSON config: {file_path}") from exc
