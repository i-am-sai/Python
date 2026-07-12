import re
import pytest
from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.reader_page import ReaderPage
from utils.logger import logger
from utils.config_reader import ConfigReader


class ShelfPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        config = ConfigReader()
        self.default_shelf = page.get_by_role("button", name="bookshelf; Default Shelf;")
        # self.read_online_button = page.get_by_role("button", name="Read Online").and_(page.locator('[data-product="944"]'))
        self.read_online_button = page.locator('a[href="/epubreader/basic-life-support-instructor-manual"][aria-label="Read Online"]')
        self.read_online_button1 = page.locator('a[href="/epubreader/advanced-cardiovascular-life-support-provider-manual-ebook50194216"][aria-label="Read Online"]')
        self.title_heading = page.get_by_role("heading",name="Basic Life Support Instructor")
        self.title_heading1 = page.get_by_role("heading",name="Advanced Cardiovascular Life Support Provider Manual")
       
        

    def open_bookshelf(self):
        logger.info("Opening Bookshelf")
        self.default_shelf.click()

    def click_read_online(self):
        self.capture_screenshot("shelf_before_scroll")
        logger.info("Scrolling to locate Read Online button")   
        self.scroll_infinite_page(self.read_online_button)

        logger.info("Opening book in Reader")
        with self.page.expect_popup() as popup_info:
            self.read_online_button.click()

        popup_page = popup_info.value
        popup_page.wait_for_load_state()
        return ReaderPage(popup_page)
   

    def verify_reader_loaded(self):
        logger.info("Verifying Reader loaded")

        expect(self.title_heading).to_be_visible()

    

       