import time
import datetime
import requests
from dmstockapi.client import Client
from requests.adapters import HTTPAdapter, Retry

"""
while True:
    t = Client(api_key='sFfSc7yrIU', api_url='http://113.108.100.57:8005', keep_alive=True)
    data = t.future_realtime(symbol='DFJ0', interval='D')
    print(datetime.datetime.now())
    print(data)
    time.sleep(1)
"""

url = "http://113.108.100.57:8005/future/china/realtime"
params = {
    "api_key": "sFfSc7yrIU",
    "interval": "D",
    "symbol": "DFJ0",
    "isdataframe": True,
}
max_retry = 5

session = requests.Session()
headers = {"Content-Type": "application/json", "Connection": "keep-alive"}
retries = Retry(total=max_retry, backoff_factor=1, status_forcelist=[502, 503, 504])
adapter: HTTPAdapter = HTTPAdapter(max_retries=retries)
session.mount("http://", adapter=adapter)

while True:
    try:
        response = session.get(url=url, params=params, headers=headers)
        print(datetime.datetime.now())
        print(response.json())
    except requests.ConnectionError:
        print(f"{max_retry + 1}次请求都失败了，即将返回空值，请耐心等待...")
    time.sleep(1)
