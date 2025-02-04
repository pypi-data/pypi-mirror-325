import json

def format_json(json_file):
    """Format and validate a JSON file."""
    try:
        with open(json_file, "r") as file:
            data = json.load(file)
        print(json.dumps(data, indent=4, sort_keys=True))
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")

if __name__ == "__main__":
    format_json("config.json")  # Change to your JSON file

