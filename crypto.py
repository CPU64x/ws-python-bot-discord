import requests
import json

class GetFinancialInfo:
    def __init__(self):
        self.cryptos = {}

    def get_crypto_price(self):
        result = "------------------------------\n"
        api_access = "https://api.coincap.io/v2/assets"
        reply = requests.get(api_access)
        data = reply.json()
    # blablabla
        return result

finance = GetFinancialInfo()

finance.get_crypto_price()