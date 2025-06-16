import yaml
import json

def load_yaml_config(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def load_json_config(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)