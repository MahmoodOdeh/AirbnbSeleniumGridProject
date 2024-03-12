import unittest
from concurrent.futures.thread import ThreadPoolExecutor
from unittest.mock import patch

import requests

from AirbnbSeleniumGridProject.infra.api_wrapper import APIWrapper
from AirbnbSeleniumGridProject.infra.browser_wrapper import BrowserWrapper
from AirbnbSeleniumGridProject.logic.tankerkoenig_api import Tankerkoenig


class TestStationData(unittest.TestCase):

    def setUp(self):
        self.response_data = Tankerkoenig.ids_api_json(self)
        self.my_api = APIWrapper()
        self.browser = BrowserWrapper()

    def test_complaint_successful(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.my_api.get_driver_url())

        response = requests.post("https://creativecommons.tankerkoenig.de/api/v4/complaint", json={
            "apikey": "cffa4fb8-7a16-cd85-7946-263722530f15",
            "id": "cb1f0588-d517-40f0-8ce3-3edadebea40d",
            "type": "wrongStatusOpen",
            "correction": ""
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"ok": True})
        return None

    def test_complaint_failure(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.my_api.get_driver_url())
        response = requests.post("https://creativecommons.tankerkoenig.de/api/v4/complaint", json={
            "apikey": "cffa4fb8-7a16-cd85-7946-263722530f15",
            "id": "cb1f0588-d517-40f0-8ce3-3edadebea40d",
            "type": "wrongStatusOpen",
            "correction": ""
        })

        # Assert the response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"ok": False})
        return None

    def test_run_grid_parallel_test_complaint_successful(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_complaint_successful, self.browser.browser_types)
        else:
            self.test_complaint_successful(self.browser.default_browser.lower())

    def test_run_grid_parallel_test_complaint_failure(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_complaint_failure, self.browser.browser_types)
        else:
            self.test_complaint_failure(self.browser.default_browser.lower())


if __name__ == '__main__':
    unittest.main()
