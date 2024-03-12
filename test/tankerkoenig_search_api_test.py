import unittest
from concurrent.futures.thread import ThreadPoolExecutor

from AirbnbSeleniumGridProject.infra.api_wrapper import APIWrapper
from AirbnbSeleniumGridProject.infra.browser_wrapper import BrowserWrapper
from AirbnbSeleniumGridProject.logic.tankerkoenig_api import Tankerkoenig


class TestJsonResponseTankerkoenig(unittest.TestCase):
    def setUp(self):
        self.json_data = Tankerkoenig.ids_api_json(self)
        self.my_api = APIWrapper()
        self.browser = BrowserWrapper()

    def test_json_structure(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.my_api.get_driver_url())
        stations = self.json_data["stations"]
        station = stations[0]
        self.assertIn("stations", self.json_data)
        self.assertIsInstance(stations, list)
        self.assertTrue(len(stations) > 0)
        self.assertIsInstance(station, dict)
        self.assertIn("country", station)
        self.assertIn("id", station)
        self.assertIn("name", station)
        self.assertIn("brand", station)
        self.assertIn("street", station)
        self.assertIn("postalCode", station)
        self.assertIn("place", station)
        self.assertIn("coords", station)
        self.assertIn("isOpen", station)
        self.assertIn("openingTimes", station)
        self.assertIn("dist", station)
        self.assertIn("fuels", station)
        self.assertIn("volatility", station)

    def test_cords_structure(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.my_api.get_driver_url())
        station = self.json_data["stations"][0]
        cords = station["coords"]
        self.assertIsInstance(cords, dict)
        self.assertIn("lat", cords)
        self.assertIn("lng", cords)

    def test_fuels_structure(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.my_api.get_driver_url())
        station = self.json_data["stations"][0]
        fuels = station["fuels"]
        for fuel in fuels:
            with self.subTest(fuel=fuel):
                last_change = fuel["lastChange"]
                self.assertIsInstance(fuel, dict)
                self.assertIn("category", fuel)
                self.assertIn("name", fuel)
                self.assertIn("price", fuel)
                self.assertIn("lastChange", fuel)
                self.assertIsInstance(last_change, dict)
                self.assertIn("amount", last_change)
                self.assertIn("timestamp", last_change)
        self.assertIsInstance(fuels, list)
        self.assertTrue(len(fuels) > 0)

    def test_run_grid_parallel_test_json_structure(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_json_structure, self.browser.browser_types)
        else:
            self.test_json_structure(self.browser.default_browser.lower())

    def test_run_grid_parallel_test_cords_structure(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_cords_structure, self.browser.browser_types)
        else:
            self.test_cords_structure(self.browser.default_browser.lower())

    def test_run_grid_parallel_test_fuels_structure(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_fuels_structure, self.browser.browser_types)
        else:
            self.test_fuels_structure(self.browser.default_browser.lower())
