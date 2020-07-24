import requests
from json import loads
params = {
    'language':'zh-chs',
    'provider':'cma',
    'unit':'c',
    'key':'',
}

url = 'http://www.thinkpage.cn/weather/api.svc/getWeather?'
res = requests.get(url,params=params)
res.encoding='utf-8'
re_json = loads(res.text)
datas = re_json['results'][0]
print(datas)
# for each in re_json['results']:
#     print(each)
