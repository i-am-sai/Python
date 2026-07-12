import logging #Python's built-in logging library.
from pathlib import Path

Path("reports/logs").mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("Playwright")
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = logging.FileHandler("reports/logs/test.log", mode="w")
    formatter = logging.Formatter("%(asctime)s || %(levelname)s | %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)







# Runs once and sets the default logging configuration.
# logging.basicConfig(   
#     filename= "reports/logs/test.log", # path where it is stored
#     level=logging.INFO,
#     format="%(asctime)s || %(levelname)s | %(message)s", # 2026-07-09 10:15:23 | INFO | Login successful
# )
# basicConfig() quietly loses a race against pytest's own logging setup; a named logger avoids the race entirely by not sharing the same global object pytest already touched.
# logger = logging.getLogger(__name__) # Gets a logger for the current file.

#from utils.logger import logger
#logger.info("Browser launched")
#logger.error("Login failed")

