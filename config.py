import json
import os

CONFIG_FILE = "aegis_config.json"

DEFAULT_CONFIG = {
    "server_url": "https://aegis-api-0z1p.onrender.com",
    "account_id": "",
    "api_key": "",
    "device_id": "win-device-001",
    "interval_sec": 3.0,
    "region": {"x": 200, "y": 150, "width": 640, "height": 400}
}

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return DEFAULT_CONFIG

def save_config(cfg):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(cfg, f, indent=4)
