import unittest
from concurrent.futures import ThreadPoolExecutor
from AirbnbSeleniumGridProject.infra.api_wrapper import APIWrapper
from AirbnbSeleniumGridProject.infra.browser_wrapper import BrowserWrapper
from AirbnbSeleniumGridProject.logic.tankerkoenig_api import Tankerkoenig


class TestStationData(unittest.TestCase):

    def setUp(self):
        self.response_data = Tankerkoenig.ids_api_json(self)
        self.my_api = APIWrapper()
        self.browser = BrowserWrapper()

    def test_station_data(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.my_api.get_driver_url())
        for station in self.response_data["stations"]:
            self.assertIn("id", station)
            self.assertIn("name", station)
            self.assertIn("brand", station)
            self.assertIn("coords", station)
            self.assertIn("isOpen", station)
            self.assertIn("dist", station)
            self.assertIn("fuels", station)
            self.assertIn("volatility", station)
        self.assertEqual(len(self.response_data["stations"]), 2)

    def test_station_data_fields(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.my_api.get_driver_url())
        for station in self.response_data["stations"]:
            self.assertIsNotNone(station["id"])
            self.assertIsNotNone(station["name"])
            self.assertIsNotNone(station["brand"])
            self.assertIsNotNone(station["coords"])
            self.assertIsNotNone(station["isOpen"])
            self.assertIsNotNone(station["dist"])
            self.assertIsNotNone(station["fuels"])
            self.assertIsNotNone(station["volatility"])
            # Check if coordinates are valid
            self.assertIn("lat", station["coords"])
            self.assertIn("lng", station["coords"])

    def test_station_fuel_prices(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.my_api.get_driver_url())
        for station in self.response_data["stations"]:
            for fuel in station["fuels"]:
                self.assertIsNotNone(fuel["category"])
                self.assertIsNotNone(fuel["name"])
                self.assertIsNotNone(fuel["price"])
                self.assertIsNotNone(fuel["lastChange"])
                self.assertRegex(fuel["lastChange"]["timestamp"], r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}")

    def test_search_center(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.my_api.get_driver_url())
        search_center = self.response_data["searchCenter"]
        self.assertIn("searchCenter", self.response_data)
        self.assertIn("lat", search_center)
        self.assertIn("lng", search_center)

    def test_license(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.my_api.get_driver_url())
        license_info = self.response_data["license"]
        self.assertIn("license", self.response_data)
        self.assertTrue(license_info.startswith("CC BY"))

    def test_run_grid_parallel_test_station_data(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_station_data, self.browser.browser_types)
        else:
            self.test_station_data(self.browser.default_browser.lower())

    def test_run_grid_parallel_test_station_data_fields(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_station_data_fields, self.browser.browser_types)
        else:
            self.test_station_data_fields(self.browser.default_browser.lower())

    def test_run_grid_parallel_test_station_fuel_prices(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_station_fuel_prices, self.browser.browser_types)
        else:
            self.test_station_fuel_prices(self.browser.default_browser.lower())

    def test_run_grid_parallel_test_search_center(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_search_center, self.browser.browser_types)
        else:
            self.test_search_center(self.browser.default_browser.lower())

    def test_run_grid_parallel_test_license(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_license, self.browser.browser_types)
        else:
            self.test_license(self.browser.default_browser.lower())




