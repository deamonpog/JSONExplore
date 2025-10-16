import glob
import json
import os

def get_json_file_paths(base_path, pattern="*.json"):
    json_files = glob.glob(os.path.join(base_path, pattern))
    return json_files

def read_json_file(file_path, encoding="utf-8"):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found at {file_path}")

    with open(file_path, "r", encoding=encoding) as file:
        data = json.load(file)
    return data
