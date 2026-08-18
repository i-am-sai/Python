
def format_timestamp():
    from datetime import datetime
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def load_config(path="config.json"):
    import json
    with open(path, "r") as file:
        return json.load(file)
    