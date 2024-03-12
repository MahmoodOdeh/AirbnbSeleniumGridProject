import concurrent.futures
import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from logic.airbnb_base_age import AirbnbBasePage


class AirbnbPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()

    def tearDown(self):
        self.browser.driver_quit()

    def test_select_from_category(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        self.airbnb = AirbnbBasePage(driver)
        time.sleep(4)
        self.airbnb.choose_house_from_category_flow()
        self.assertIn('Airbnb | יחידות נופש להשכרה, בקתות, בתי חוף ועוד', driver.title, "the title is not correct")

    def test_run_grid_parallel_select_from_category(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_select_from_category, self.browser.browser_types)
        else:
            self.test_select_from_category(self.browser.default_browser.lower())
