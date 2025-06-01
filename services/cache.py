import json
import os

LOCAL_FILE = os.path.join(os.path.dirname(__file__), "../data/local_data.json")

def load_local_data(table_name: str):
    with open(LOCAL_FILE, encoding="utf-8") as f:
        data = json.load(f)
    return data.get(table_name, [])
