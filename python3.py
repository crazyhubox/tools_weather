#!/usr/local/bin/python3
# encoding:utf-8
import requests
from re import search,compile


url = "https://www.baidu.com/"
res = requests.get(url)
print(res.status_code)
