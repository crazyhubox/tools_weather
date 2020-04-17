#!/usr/local/bin/python3
# encoding:utf-8
import json
import re
import time
import requests



class GetCityNum:
    t1 = str(round(time.time()))
    headers = {
        'Cookie':f'f_city=%E8%B4%B5%E9%98%B3%7C101260101%7C; vjuids=d7494d7fc.1702d7094f2.0.671014907ea4c; vjlast=1581310318.1581310318.30; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1581310318; cityListHty=101130613%7C101310201%7C101260101%7C101010100%7C101020100%7C101280101%7C101280601%7C101010300; Wa_lvt_51=1581319721; cityListCmp=%E5%8C%97%E4%BA%AC-101010100-20200227%7C%E4%B8%8A%E6%B5%B7-101020100-20200228%7C%E5%B9%BF%E5%B7%9E-101280101-20200229%7C%E6%B7%B1%E5%9C%B3-101280601-20200301%2Cdefault%2C20200227; Wa_lvt_1=1581308047,1581310507,1581430179,1582780936; Wa_lpvt_1={t1}',
        'Host':'d1.weather.com.cn',
        'Referer':'http://www.weather.com.cn/',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    }
    
    def __init__(self, name):
      self.name = name

    def getrequest(self):
        t = str(time.time()).replace('.', '')[:-3]
        url = f'http://toy1.weather.com.cn/search?'
        param = {
            'cityname':self.name,
            'callback':'success_jsonpCallback',
            '_':t,
        }
        res = requests.get(url,params=param)#经过postman测试不需要headers
        res.encoding = 'utf-8'

        result = re.search(r'\[.+\]',res.text,re.S)[0]
        data = json.loads(result)
        str_1 = data[0]['ref']
        str_2 = str_1[str_1.rindex('~')+1:]
        num = re.search(r'\d+',data[0]['ref'])[0]
        return num,str_2

    @classmethod
    def encourage(cls):
        url = 'https://v1.hitokoto.cn/?'
        params = {
            'c':'a',
            'encode':'json',
        }
        res = requests.get(url,params=params)
        data=  json.loads(res.text)
        content = data['hitokoto']
        author = data['creator']
        print(author+': '+content)

    @classmethod
    def poem(cls):
        url = 'https://v2.jinrishici.com/one.json'
        headers = {
            'accept':'*/*',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'origin':'http://47.114.165.39:8000',
            'referer':'http://47.114.165.39:8000/choice?key=p',
            'sec-fetch-dest':'empty',
            'sec-fetch-mode':'cors',
            'sec-fetch-site':'cross-site',
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        }
        res = requests.get(url=url,params=None,headers=headers)
        # print(res.status_code)
        if res.status_code == 200:
            result = res.text
            data = json.loads(result)
            contents = data['data']['origin']['content']
            translate = data['data']['origin']['translate']
            for each in contents:
                print(each)
            print('='*100)
            for each in translate:
                print(each)
        else:
            print('响应异常')


