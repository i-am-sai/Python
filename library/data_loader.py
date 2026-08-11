from pathlib import Path
from utils import Logger
import logging

log = Logger("reports/test.log")
log.info("Sucesss")  # Logging using cutom logger class

reports_dir = Path("reports")
reports_dir.mkdir(exist_ok=True)

log_file = reports_dir / "test.log"

logging.basicConfig(filename=log_file, level=logging.INFO)
logging.info("Test started")     # Logging using built in class


test_results = ["choice 1: pass", "choice 2: fail"]

try:
    with open("reports/test.txt", "a") as file:
        for result in test_results:
            file.write(result + "\n")
except FileNotFoundError as e:
    print(f"File not found: {e}")
else:
    print("Upload")
finally:
    print("Done")


#json.load() -> json file -> Dict
#json.loads() -> json string -> Dict
#json.dump() -> python -> json file (write a json file)
#json.dumps() -> python -> json
import json

with open("data/books.json", "r") as file:
    data = json.load(file)

print(data)
print(data["title"])

book_details = {
    "book_id": "2",
    "title": "Sapiens",
    "author": "Bhagath"
}

with open("data/books.json", "a") as file:
    json.dump(book_details, file, indent=4)
   

json_s = '{"book_id": "2", "title": "Sapiens", "author": "Bhagath"}'

json_ = {"book_id": "2", "title": "Sapiens", "author": "Bhagath"}
da = json.loads(json_s)
print(da)

sa = json.dumps(json_)
print(sa)





