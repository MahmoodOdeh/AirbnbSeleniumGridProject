import concurrent.futures
import unittest

from logic.world_page import AirbnbWorldPage
from infra.browser_wrapper import BrowserWrapper
from logic.airbnb_base_age import AirbnbBasePage



class AirbnbPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()

    def tearDown(self):
        self.browser.driver_quit()

    def test_change_language(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        self.airbnb = AirbnbBasePage(driver)
        self.airbnb.press_word_btn()
        self.language = AirbnbWorldPage(driver)
        self.language.press_language_btn()
        self.assertIn('Airbnb | Vacation rentals, cabins, beach houses, & more', driver.title,
                      "the title is not correct")

    def test_run_grid_parallel_st_press_word_btn(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:

            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_change_language, self.browser.browser_types)
        else:

            self.test_change_language(self.browser.default_browser.lower())
