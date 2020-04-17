#!/usr/local/bin/python3
# encoding:utf-8

import requests
import json
from scrapy.selector import Selector
import time
import re

url = 'https://kns.cnki.net/KRS/KRSHandler.ashx?'
t = str(time.time()).replace('.', '')[:-3]
params = {
	'userName':'970161120@qq.com',
	'cnkiUserKey':'ab03d57b-fde3-fca7-4544-a5f4ec144b9d',
	'keyWord':'c++',
	'td':t,
}

headers = {
	'Host':'kns.cnki.net',
	'Referer':'https://kns.cnki.net/kns/brief/brief.aspx?pagename=ASP.brief_default_result_aspx&isinEn=1&dbPrefix=SCDB&dbCatalog=%e4%b8%ad%e5%9b%bd%e5%ad%a6%e6%9c%af%e6%96%87%e7%8c%ae%e7%bd%91%e7%bb%9c%e5%87%ba%e7%89%88%e6%80%bb%e5%ba%93&ConfigFile=SCDBINDEX.xml&research=off&t=1584014592581&keyValue=scrapy&S=1&sorttype=',
	'Sec-Fetch-Mode':'no-cors',
	'Sec-Fetch-Site':'same-origin',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
}

res = requests.get(url=url,params=params,headers=headers)
print(res.status_code)
results = res.text
data = re.search(r'{.+}',results,re.S)[0]  
data_json = json.loads(data)["recommendInfo"]
for each in data_json:
	print(each['TitleName'])
	print(each['DownloadCount'])
# print(data_json) c