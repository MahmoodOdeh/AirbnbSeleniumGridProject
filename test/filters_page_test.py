import concurrent.futures
import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from logic.airbnb_base_age import AirbnbBasePage
from logic.filters_page import AirbnbFilterPage


class AirbnbPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()

    def tearDown(self):
        self.browser.driver_quit()

    def test_filter_by_minimum_and_maximum_price(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        self.airbnb = AirbnbBasePage(driver)
        self.airbnb.press_filter_btn()
        self.filter = AirbnbFilterPage(driver)
        self.filter.minimum_fill("300")
        self.filter.maximum_fill("5000")
        self.filter.press_show_btn()
        self.assertEqual(self.filter.get_minimum_price_value(), "300", "Minimum price value is incorrect")
        self.assertEqual(self.filter.get_maximum_price_value(), "5000", "Maximum price value is incorrect")

    def test_st_press_filter_and_clear_btn(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        self.airbnb = AirbnbBasePage(driver)
        self.airbnb.press_filter_btn()
        self.filter = AirbnbFilterPage(driver)
        self.filter.minimum_fill("300")
        self.filter.maximum_fill("5000")
        self.filter.press_clear_btn()
        self.assertEqual(self.filter.get_minimum_price_value(), "300", "Minimum price value is incorrect")
        self.assertEqual(self.filter.get_maximum_price_value(), "5000", "Maximum price value is incorrect")

    def test_filter_by_minimum_and_maximum_price_conversely(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        self.airbnb = AirbnbBasePage(driver)
        self.airbnb.press_filter_btn()
        self.filter = AirbnbFilterPage(driver)
        self.filter.minimum_fill("10000")
        self.filter.maximum_fill("200")
        self.filter.press_show_btn()
        self.assertEqual(self.filter.get_minimum_price_value(), "10000", "Minimum price value is incorrect")
        self.assertEqual(self.filter.get_maximum_price_value(), "200", "Maximum price value is incorrect")

    def test_filter_by_minimum_and_maximum_price_minus(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        self.airbnb = AirbnbBasePage(driver)
        self.airbnb.press_filter_btn()
        self.filter = AirbnbFilterPage(driver)
        self.filter.minimum_fill("-1000")
        self.filter.maximum_fill("-1000")
        self.filter.press_show_btn()
        self.assertEqual(self.filter.get_minimum_price_value(), "-1000", "Minimum price value is incorrect")
        self.assertEqual(self.filter.get_maximum_price_value(), "-1000", "Maximum price value is incorrect")

    def test_filter_navigate_bar(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        self.airbnb = AirbnbBasePage(driver)
        self.airbnb.press_filter_btn()
        self.filter = AirbnbFilterPage(driver)
        self.filter.navigate_press()
        self.filter.press_show_btn()
        self.assertIn('Airbnb | יחידות נופש להשכרה, בקתות, בתי חוף ועוד', driver.title, "the title is not correct")

    def test_run_grid_parallel_filter_by_minimum_and_maximum_price(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:

            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_filter_by_minimum_and_maximum_price, self.browser.browser_types)
        else:
            self.test_filter_by_minimum_and_maximum_price(self.browser.default_browser.lower())

    def test_run_grid_parallel_filter_by_minimum_and_maximum_price_conversely(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:

            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_filter_by_minimum_and_maximum_price_conversely, self.browser.browser_types)
        else:

            self.test_filter_by_minimum_and_maximum_price_conversely(self.browser.default_browser.lower())

    def test_run_grid_parallel_st_press_filter_and_clear_btn(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:

            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_st_press_filter_and_clear_btn, self.browser.browser_types)
        else:

            self.test_st_press_filter_and_clear_btn(self.browser.default_browser.lower())

    def test_run_grid_parallel_filter_by_minimum_and_maximum_price_minus(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:

            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_filter_by_minimum_and_maximum_price_minus, self.browser.browser_types)
        else:

            self.test_filter_by_minimum_and_maximum_price_minus(self.browser.default_browser.lower())

    def test_run_grid_parallel_filter_by_navigate_bar(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:

            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_filter_navigate_bar, self.browser.browser_types)
        else:

            self.test_filter_navigate_bar(self.browser.default_browser.lower())

    def test_ran_all_filters_page_test(self):
        self.test_run_grid_parallel_filter_by_minimum_and_maximum_price()
        self.test_run_grid_parallel_filter_by_minimum_and_maximum_price_conversely()
        self.test_run_grid_parallel_st_press_filter_and_clear_btn()
        self.test_run_grid_parallel_filter_by_minimum_and_maximum_price_minus()
        self.test_run_grid_parallel_filter_by_navigate_bar()
