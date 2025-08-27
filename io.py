# nucleus_tensegrity/io.py

import json
import os

def load_custom_isoform(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    with open(filepath, "r") as f:
        data = json.load(f)

    required = ["name", "nodes", "edges"]
    for key in required:
        if key not in data:
            raise ValueError(f"Missing required key '{key}' in file")

    return data["name"], data["nodes"], data["edges"]

