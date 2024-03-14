import unittest
from concurrent.futures.thread import ThreadPoolExecutor
import sys

sys.path.append(r'AirbnbSeleniumGridProject\\infra')
sys.path.append(r'AirbnbSeleniumGridProject\\logic')




from infra.api_wrapper import APIWrapper
from infra.browser_wrapper import BrowserWrapper
from logic.tankerkoenig_api import Tankerkoenig


class TestJsonResponseTankerkoenig(unittest.TestCase):
    def setUp(self):
        self.json_data = Tankerkoenig.ids_api_json(self)
        self.my_api = APIWrapper()
        self.browser = BrowserWrapper()

    def test_count_accuracy(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.my_api.get_driver_url())
        total_count = (
                self.json_data["E5"]["count"] +
                self.json_data["E10"]["count"] +
                self.json_data["Diesel"]["count"]
        )

        self.assertEqual(total_count, len(range(1, total_count + 1)))

    def test_license_website(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.my_api.get_driver_url())
        self.assertTrue(self.json_data["license"].startswith("CC BY"))
        self.assertFalse("creativecommons.org" in self.json_data["license"])

    def test_api_version_format(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.my_api.get_driver_url())
        version_parts = self.json_data["apiVersion"].split(".")
        self.assertEqual(len(version_parts), 3)
        self.assertTrue(all(part.isdigit() for part in version_parts))

    def test_unique_timestamps(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.my_api.get_driver_url())
        timestamps = set()
        for _ in range(10000):
            timestamp = self.json_data["timestamp"]
            timestamps.add(timestamp)

        self.assertEqual(len(timestamps), 1, "Timestamps are not unique")

    def test_run_grid_parallel_test_count_accuracy(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_count_accuracy, self.browser.browser_types)
        else:
            self.test_count_accuracy(self.browser.default_browser.lower())

    def test_run_grid_parallel_test_license_website(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_license_website, self.browser.browser_types)
        else:
            self.test_license_website(self.browser.default_browser.lower())

    def test_run_grid_parallel_test_api_version_format(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_api_version_format, self.browser.browser_types)
        else:
            self.test_api_version_format(self.browser.default_browser.lower())

    def test_run_grid_parallel_test_unique_timestamps(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_unique_timestamps, self.browser.browser_types)
        else:
            self.test_unique_timestamps(self.browser.default_browser.lower())
