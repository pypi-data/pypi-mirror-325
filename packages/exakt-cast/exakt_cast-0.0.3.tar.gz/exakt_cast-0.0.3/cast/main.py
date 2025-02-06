from pathlib import Path
import subprocess
import os
import json


def main():
    os.chdir(os.path.dirname(__file__))
    home = Path.home()
    base_dir = os.path.join(home, "Documents", "Cast")
    sub_dirs = [
        os.path.join(base_dir, "data", "source"),
        os.path.join(base_dir, "data", "export"),
        os.path.join(base_dir, "queries"),
         os.path.join(base_dir, "configs"),
    ]
    for sub_dir in sub_dirs:
        os.umask(0)
        os.makedirs(os.path.join(base_dir, sub_dir), exist_ok=True,mode=0o777)

    json_content = {
        "missing_values": ["NaN", "None", "", " ", "\t", "N/A", "NULL", "NA", "n/a", "missing", "unknown", "Undefined", "-", "--", "?"],
        "numeric_separator": ",",
        "interactive_limit": 2000000,
    }

    # Path to the JSON file
    json_file_path = os.path.join(base_dir, "settings.json")

    if not os.path.exists(json_file_path):
        # Write the content to the JSON file
        with open(json_file_path, "w") as json_file:
            json.dump(json_content, json_file, indent=4)

    subprocess.run(["streamlit", "run", "app.py"])
