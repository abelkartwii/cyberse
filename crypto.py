import requests

class APIService:
    def retrieve_json(self, url):
        try:
            response = requests.get(url)
            return response.json()
        except ConnectionError:
            return {}

    def parse_json(self, data):
        return {
            coin_name = data["name"],
            market_cap = data["marketCap"],
            price = data["price"]
        }

    def filter_json(self, raw_json):
        filtered_json = map(lambda data: self.parse_json(data),
                            raw_json["data"]["coins"])
        return filetered_json