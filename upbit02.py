import requests  # pip install 필요
import pyupbit  # pip install 필요
# import json
# import time

url = "https://api.upbit.com/v1/market/all?isDetails=false"

headers = {"accept": "application/json"}

res = requests.get(url, headers=headers)

result = res.json()

print(result[0]['market'])

coinTicker = pyupbit.get_tickers(fiat="KRW")

print(coinTicker)
