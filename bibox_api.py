import hashlib
import hmac
import json

import requests


class Bibox:

    def __init__(self, api_key, secret_key):
        """Constructor"""
        self.__api_key = api_key
        self.__secret_key = secret_key

    def __create_md5_signature(self, message):
        return hmac.new(self.__secret_key.encode('utf-8'), message.encode('utf-8'), hashlib.md5).hexdigest()

    def __post(self, cmd, body):
        cmds = json.dumps([{
            "cmd": cmd,
            "body": body
        }])
        sign = self.__create_md5_signature(cmds)
        data = {
            "cmds": cmds,
            "apikey": self.__api_key,
            "sign": sign
            }
        response = requests.post('https://api.bibox.com/v1/' + cmd.split('/')[0], data=data)
        return response.json()

    # User

    def user_info(self):
        return self.__post('user/userInfo', {})

    # Transfer

    def coin_list(self):
        return self.__post('transfer/coinList', {})

    def deposit_address(self, token):
        params = {"coin_symbol": token}
        return self.__post('transfer/transferIn', params)

    def withdrawal(self, token):
        params = {"coin_symbol": token}
        return self.__post('transfer/transferOutInfo', params)

    def deposit_list(self, token, status, page, size):
        params = {"search": token,
                  "filter_type": status,
                  "page": page,
                  "size": size}
        return self.__post('transfer/transferInList', params)

    def withdrawal_list(self, token, status, page, size):
        params = {"search": token,
                  "filter_type": status,
                  "page": page,
                  "size": size}
        return self.__post('transfer/transferOutList', params)

    def assets(self, select):
        params = {"select": select}
        return self.__post('transfer/assets', params)



# Usage

bibox = Bibox('fb5120917c3971b1a7e5c998c4d761bcfa9676c7', '24856b63ee7db428b3d93b8623a77de630676e8b')

# print(bibox.user_info())
# print(bibox.coin_list())
# print(bibox.deposit_address('BTC'))
# print(bibox.withdrawal('BTC'))
# print(bibox.deposit_list('BTC', 0, 1, 10))
# print(bibox.withdrawal_list('BTC', 0, 1, 10))
# print(bibox.assets(1))