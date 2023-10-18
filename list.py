import json
import os

def get_url_list(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
             json.dump({'urls': []}, file)
    with open(file_path, 'r') as file:
        data = json.load(file)

    if "urls" in data and isinstance(data["urls"], list):
        return data["urls"]

def write_url_list(file_path, url_list):
        with open(file_path, 'w') as file:
            json.dump({'urls': url_list}, file)