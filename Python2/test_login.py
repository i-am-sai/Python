from Python2.utils import format_timestamp, load_config

config = load_config()
timestamp = format_timestamp()

print(f"Running test at {timestamp} against {config['base_url']}")