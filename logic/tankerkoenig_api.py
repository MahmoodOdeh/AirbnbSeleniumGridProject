from infra.api_wrapper import APIWrapper


class Tankerkoenig:

    def __init__(self, api_object):
        self.my_api = api_object

    def search_api_json(self):
        self.my_api = APIWrapper()
        result = self.my_api.api_get_request(
            f'https://creativecommons.tankerkoenig.de/api/v4/stations/search?apikey=cffa4fb8-7a16-cd85-7946-263722530f15&lat=48.8&lng=9.24&rad=10')
        return result.json()

    def postalcodes_api_json(self):
        self.my_api = APIWrapper()
        result = self.my_api.api_get_request(
            f'https://creativecommons.tankerkoenig.de/api/v4/stations/ids?apikey=cffa4fb8-7a16-cd85-7946-263722530f15&ids=92f703e8-0b3c-46da-9948-25cb1a6a1514%2C83d5ac80-4f23-4106-b054-7c7704bfcb95&lat=48.8&lng=9.24')
        return result.json()

    def stats_api_json(self):
        self.my_api = APIWrapper()
        result = self.my_api.api_get_request(
            f'https://creativecommons.tankerkoenig.de/api/v4/stats?apikey=cffa4fb8-7a16-cd85-7946-263722530f15')
        return result.json()

    def ids_api_json(self):
        self.my_api = APIWrapper()
        result = self.my_api.api_get_request(
            f'https://creativecommons.tankerkoenig.de/api/v4/stations/ids?apikey=cffa4fb8-7a16-cd85-7946-263722530f15&ids=92f703e8-0b3c-46da-9948-25cb1a6a1514%2C83d5ac80-4f23-4106-b054-7c7704bfcb95&lat=48.8&lng=9.24')
        return result.json()

    def complaint_api_json(self):
        self.my_api = APIWrapper()
        result = self.my_api.api_post_request(
            f'https://creativecommons.tankerkoenig.de/api/v4/complaint')
        return result.json()