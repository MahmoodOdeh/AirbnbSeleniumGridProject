import unittest
from concurrent.futures.thread import ThreadPoolExecutor

from infra.api_wrapper import APIWrapper
from infra.browser_wrapper import BrowserWrapper
from logic.tankerkoenig_api import Tankerkoenig


class TestStationData(unittest.TestCase):

    def setUp(self):
        self.response = Tankerkoenig.ids_api_json(self)
        self.my_api = APIWrapper()
        self.browser = BrowserWrapper()

    def test_response_keys(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.my_api.get_driver_url())
        expected_keys = ["stations", "searchCenter", "apiVersion", "timestamp", "license"]
        self.assertCountEqual(expected_keys, self.response.keys())
        print(self.response.keys())

    def test_station_structure(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.my_api.get_driver_url())
        driver = self.browser.get_driver(browser_type)
        driver.get(self.my_api.get_driver_url())
        for station in self.response["stations"]:
            self.assertIsInstance(station["country"], str)
            self.assertIsInstance(station["id"], str)
            self.assertIsInstance(station["name"], str)
            self.assertIsInstance(station["brand"], str)
            self.assertIsInstance(station["street"], str)
            self.assertIsInstance(station["postalCode"], str)
            self.assertIsInstance(station["place"], str)
            self.assertIsInstance(station["coords"], dict)
            self.assertIsInstance(station["isOpen"], bool)
            self.assertIsInstance(station["openingTimes"], list)
            self.assertIsInstance(station["dist"], float)
            self.assertIsInstance(station["fuels"], list)
            self.assertIsInstance(station["volatility"], int)

    def test_search_center_structure(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.my_api.get_driver_url())
        self.assertIsInstance(self.response["searchCenter"], dict)
        self.assertIn("lat", self.response["searchCenter"])
        self.assertIn("lng", self.response["searchCenter"])

    def test_api_version_format(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.my_api.get_driver_url())
        self.assertRegex(self.response["apiVersion"], r"\d+\.\d+\.\d+")

    def test_license_format(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.my_api.get_driver_url())
        self.assertTrue(self.response["license"].startswith("CC BY"))

    def test_station_cords_structure(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.my_api.get_driver_url())
        for station in self.response["stations"]:
            self.assertIn("lat", station["coords"])
            self.assertIn("lng", station["coords"])

    def test_station_opening_times_structure(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.my_api.get_driver_url())
        for station in self.response["stations"]:
            for time in station["openingTimes"]:
                self.assertIn("days", time)
                self.assertIsInstance(time["days"], list)
                self.assertIn("times", time)
                self.assertIsInstance(time["times"], list)
                for t in time["times"]:
                    self.assertIn("open", t)
                    self.assertIsInstance(t["open"], str)
                    self.assertIn("close", t)
                    self.assertIsInstance(t["close"], str)

    def test_run_grid_parallel_test_response_keys(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_response_keys, self.browser.browser_types)
        else:
            self.test_response_keys(self.browser.default_browser.lower())

    def test_run_grid_parallel_test_station_structure(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_station_structure, self.browser.browser_types)
        else:
            self.test_station_structure(self.browser.default_browser.lower())

    def test_run_grid_parallel_test_search_center_structure(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_search_center_structure, self.browser.browser_types)
        else:
            self.test_search_center_structure(self.browser.default_browser.lower())

    def test_run_grid_parallel_test_api_version_format(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_api_version_format, self.browser.browser_types)
        else:
            self.test_api_version_format(self.browser.default_browser.lower())

    def test_run_grid_parallel_test_license_format(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_license_format, self.browser.browser_types)
        else:
            self.test_license_format(self.browser.default_browser.lower())

    def test_run_grid_parallel_test_station_cords_structure(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_station_cords_structure, self.browser.browser_types)
        else:
            self.test_station_cords_structure(self.browser.default_browser.lower())

    def test_run_grid_parallel_test_station_opening_times_structure(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_station_opening_times_structure, self.browser.browser_types)
        else:
            self.test_station_opening_times_structure(self.browser.default_browser.lower())







