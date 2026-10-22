from pathlib import Path
import logging

class Logger:
    # def __init__(self, path):
    #     self.path = path

    # def info(self, message):
    #     with open(self.path, "w") as file:
    #         file.write(f"[INFO] {message}\n")
    #         # print(f"[INFO] {message}")

    def info(self, message):
            print(f"[INFO] {message}")
    
    def warning(self, message):
        print(f"[WARNING] {message}")
    
    def error(self, message):
        print (f"[ERROR] {message}")
    
class Validator:
    def is_valid_id(self, value):
        if value > 0:
            return True
        else:
            return False
    
    def book_exists(library, book_id):
        for book in library.books:
            if book.book_id == book_id:
                return True
        return False
    
    def member_exists(library, member_id):
        for member in library.members:
            if member.member_id == member_id:
                return True
        return False
    
# a = Validator()
# print(a.is_valid_id(-1))

# print(Validator.__mro__) # Helps for debugging : This will show you the exact chain Python searches through: (<class '__main__.Validator'>, <class 'object'>)


reports_dir = Path("reports")
reports_dir.mkdir(exist_ok=True)

log_file = reports_dir / "test.log"

logging.basicConfig(filename=log_file, level=logging.INFO)
logging.info("Test started")     # Logging using built in class
logger = logging.getLogger("Library")
logger.setLevel(logging.INFO)