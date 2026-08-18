from pathlib import Path

#pathlib treats paths as objects not plain strings: this fits python overall style better.

path = Path("reports") / "screenshots" / "test1.png"
print(path)

path = Path("summary.txt")

if path.exists():
    print("File exists")

path.parent          # the folder containing this file
path.name             # "config.json"
path.suffix           # ".json"
path.stem             # "config" (name without extension)

# os way
import os
path = os.path.join("reports", "screenshots", "test1.png")
if os.path.exists(path):
    print("exists")

# pathlib way
from pathlib import Path
path = Path("reports") / "screenshots" / "test1.png"
if path.exists():
    print("exists")

# Creating directories:
Path("reports/screenshots").mkdir(parents=True, exist_ok=True)

#Reading/writing files — pathlib even has shortcuts:
content = Path("data.txt").read_text()
print(content)
Path("Data.txt").write_text("Test Completed")

#Listing files
for file in Path("reports").iterdir():
    print(file)

    #Direct comparison — same task, both ways
# os way
import os
path = os.path.join("reports", "screenshots", "test1.png")
if os.path.exists(path):
    print("exists")

# pathlib way
from pathlib import Path
path = Path("reports") / "screenshots" / "test1.png"
if path.exists():
    print("exists")

#Both work identically. pathlib is generally preferred in modern Python code (it's cleaner, object-oriented, and less error-prone with separators) — but you'll still see os everywhere in existing codebases, GitHub Actions examples, and older tutorials, so you need to recognize both.

from pathlib import Path

screenshot_dir = Path("reports") / "screenshots"
screenshot_dir.mkdir(parents=True, exist_ok=True)

screenshot_path = screenshot_dir / "login_test_failure.png"
# page.screenshot(path=str(screenshot_path))

#Note the str() — Playwright's screenshot() expects a plain string path, so you convert the Path object at the point of use. This is a common small gotcha: pathlib objects aren't automatically strings everywhere.
