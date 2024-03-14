import requests

from infra.config_handler import ConfigHandler


class APIWrapper:
    def __init__(self):
        self.response = None
        self.my_request = requests
        config_file_path = 'C:/Users/odehm/Desktop/seleniumGrid/airbnb/config.json'
        self.config_handler = ConfigHandler(config_file_path)
        self.url_api = self.config_handler.get_config_value('url_api')

    def api_get_request(self, url_api):
        self.response = self.my_request.get(url_api)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def api_post_request(self, url_api, data=None):
        self.response = self.my_request.post(url_api, json=data)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def get_driver_url(self):
        return self.url_api
