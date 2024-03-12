import concurrent.futures
import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from logic.airbnb_base_age import AirbnbBasePage
from logic.search_page import AirbnbSearchPage
from logic.who_page import AirbnbWhoPage


class AirbnbPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()

    def test_search_by_agenda(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        self.airbnb = AirbnbBasePage(driver)
        self.airbnb.press_check_in_btn()
        self.filter = AirbnbSearchPage(driver)
        self.filter.press_date_to_check_in()
        self.airbnb.press_check_out_btn()
        self.filter.press_date_to_check_out()
        self.airbnb.press_search_btn()
        self.assertIn('Airbnb | יחידות נופש להשכרה, בקתות, בתי חוף ועוד', driver.title, "the title is not correct")

    def test_search_by_agenda_the_dates_wrong(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        self.airbnb = AirbnbBasePage(driver)
        self.airbnb.press_check_in_btn()
        self.filter = AirbnbSearchPage(driver)
        self.filter.press_date_to_check_out()
        self.airbnb.press_check_out_btn()
        self.filter.press_date_to_check_in()
        self.filter.press_date_to_check_out()
        self.airbnb.press_search_btn()
        self.assertIn('Airbnb | יחידות נופש להשכרה, בקתות, בתי חוף ועוד', driver.title, "the title is not correct")

    def test_search_by_generation(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        self.airbnb = AirbnbBasePage(driver)
        self.airbnb.press_who_btn()
        self.filter = AirbnbWhoPage(driver)
        self.filter.select_generation_flow()
        self.airbnb.press_search_btn()
        self.assertIn('Airbnb | יחידות נופש להשכרה, בקתות, בתי חוף ועוד', driver.title, "the title is not correct")

    def test_run_grid_parallel_search_by_agenda(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:

            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_search_by_agenda, self.browser.browser_types)
        else:

            self.test_search_by_agenda(self.browser.default_browser.lower())

    def test_run_grid_parallel_search_by_agenda_the_dates_wrong(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:

            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_search_by_agenda_the_dates_wrong, self.browser.browser_types)
        else:

            self.test_search_by_agenda_the_dates_wrong(self.browser.default_browser.lower())

    def test_run_grid_parallel_search_by_generation(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:

            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_search_by_generation, self.browser.browser_types)
        else:

            self.test_search_by_generation(self.browser.default_browser.lower())

    def test_ran_all_search_page_test(self):
        self.test_run_grid_parallel_search_by_agenda()
        self.test_run_grid_parallel_search_by_agenda_the_dates_wrong()
        self.test_run_grid_parallel_search_by_generation()
