import pytest
import shutil
from playwright.sync_api import expect
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
from utils.logger import logger

@pytest.fixture(scope="session", autouse=True)
def clean_reports():
    shutil.rmtree("reports/screenshots", ignore_errors=True)
    # shutil.rmtree("reports/logs", ignore_errors=True)
    yield

@pytest.fixture(scope="session")
def authenticated_state(browser):
    config = ConfigReader()
    context = browser.new_context()
    page = context.new_page()
    login_page = LoginPage(page)

    logger.info("Performing one-time login for session")
    login_page.navigate(config.get("base_url"))
    login_page.accept_cookies()
    login_page.click_login()
    login_page.accept_cookies()
    login_page.enter_credentials(config.username, config.password)
    login_page.click_signin()

    login_page.capture_screenshot("After clicking Sign In")
    expect(page).to_have_url(config.get("bookshelf_url"))
    expect(page.get_by_text("Please login")).not_to_be_visible()   # explicit negative check
    
   # Let any trailing redirects/cookie-setting requests fully settle
    page.wait_for_load_state("networkidle")
    
    cookies = context.cookies()
    auth_cookie = next((c for c in cookies if c["name"] == "SimpleSAMLAuthToken"), None)

    if not auth_cookie:
        raise Exception(
            "Login flow completed but SimpleSAMLAuthToken cookie was not set — "
            "authentication state is invalid, refusing to save storage_state."
        )

    logger.info(f"SimpleSAMLAuthToken confirmed present, saving storage state {auth_cookie}")
    state = context.storage_state(path="reports/.auth/auth_state.json")
    context.close()
    return state

@pytest.fixture
def logged_in_page(browser, authenticated_state):
    config = ConfigReader()
    context = browser.new_context(storage_state="reports/.auth/auth_state.json")
    page = context.new_page()
    page.goto(config.get("bookshelf_url"))
    yield page
    context.close()











# import shutil — Python's built-in module for higher-level file operations; os can delete single files, but shutil is what you use for deleting entire folders and their contents at once.

# @pytest.fixture(scope="session", autouse=True) — two things happening here:

# scope="session" means this runs once for the entire test run, not once per test — you want cleanup to happen a single time, at the very start, not repeated before every individual test.
# autouse=True means every test automatically triggers this fixture without needing to list it as a parameter — you'll never write def test_login(clean_reports, page):, it just happens silently in the background for the whole session.
# yield — this is the same pattern from your browser/page fixtures. Everything before yield runs as setup (the cleanup, in this case), and since there's no code after yield, there's no teardown step — the fixture just finishes once the whole session ends.

# tests/conftest.py
# No custom fixtures needed yet.
# pytest-playwright already provides:
# browser
# context
# page


