from pathlib import Path # Used to work with file and folder paths in a platform-independent way (Mean VS code, Gihub actions, Linux, Wind)

def take_screenshot(page, name): # page: Playwright page object and name: screenshot filename
    screenshot_dir = Path("reports/screenshots")
    screenshot_dir.mkdir(parents=True, exist_ok=True) # parents=True → Create parent folders if missing and exist_ok=True → Don't fail if the folder already exists.

    page.screenshot(path=screenshot_dir / f"{name}.png")


#Calling method:  take_screenshot(page, "login_failed")











# from pathlib import Path

# class ScreenshotHelper:
#     def __init__(self, base_dir="reports/screenshots"):
#         self.base_dir = Path(base_dir)
#         self.base.mkdir(parents=True, exist_ok=True)
    
#     def save(self, page, name):
#         path = self.base_dir / f"{name}.png"
#         page.screenshot(path=str(path))
#         return path

