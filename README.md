# bibox-api-python
Python wrapper for Bibox REST API   
> Full docs are here https://github.com/Biboxcom/api_reference/wiki/home_en

### Usage

```python
from bibox_api import *

api_key = '<your api key>'
secret_key = '<your secret key>'

bibox = Bibox(api_key, secret_key)
```

##### Reference

```python
print(bibox.user_info())
print(bibox.coin_list())
print(bibox.deposit_address('BTC'))
print(bibox.withdrawal('BTC'))
print(bibox.deposit_list('BTC', 0, 1, 10))
print(bibox.withdrawal_list('BTC', 0, 1, 10))
print(bibox.assets(1))
```

