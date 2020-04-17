#!/usr/local/bin/python3
# encoding:utf-8
import json
import re
import time
import requests
from weather.GetCityNum import GetCityNum

class GetSight_province:
    t1 = str(round(time.time()))
    headers = {
        'Cookie':f'f_city=%E8%B4%B5%E9%98%B3%7C101260101%7C; vjuids=d7494d7fc.1702d7094f2.0.671014907ea4c; vjlast=1581310318.1581310318.30; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1581310318; cityListHty=101130613%7C101310201%7C101260101%7C101010100%7C101020100%7C101280101%7C101280601%7C101010300; Wa_lvt_51=1581319721; cityListCmp=%E5%8C%97%E4%BA%AC-101010100-20200227%7C%E4%B8%8A%E6%B5%B7-101020100-20200228%7C%E5%B9%BF%E5%B7%9E-101280101-20200229%7C%E6%B7%B1%E5%9C%B3-101280601-20200301%2Cdefault%2C20200227; Wa_lvt_1=1581308047,1581310507,1581430179,1582780936; Wa_lpvt_1={t1}',
        'Host':'d1.weather.com.cn',
        'Referer':'http://www.weather.com.cn/weather1d/101260101.shtml',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    }

    def getSight(self):
        t = str(time.time()).replace('.', '')[:-3]
        id_num,name = self.get_city_num()
        # url = f'http://d1.weather.com.cn/travel_rank/3A10126.html?_={t}'
        url = f'http://d1.weather.com.cn/travel_rank/3A{id_num}.html?_={t}'
        res = requests.get(url,headers=self.headers)
        res.encoding='utf-8'
        print(res.status_code)
        result = re.search(r'{.+}',res.text)[0]
        dada = json.loads(result)
        print('当前城市所在省区:',name)
        for key in dada:
            # print(key,dada[key])
            print(dada[key])

    @classmethod
    def get_city_num(cls):
        city = input('查询城市:')
        data = GetCityNum(city)
        id_num,pro_name = data.getrequest()
        province_id = id_num[:-4]
        return province_id,pro_name


#省编号 市区编号
# 10126 0101