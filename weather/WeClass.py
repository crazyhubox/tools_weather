#!/usr/local/bin/python3
# encoding:utf-8
import json
import re
import time
import requests
from weather.GetCityNum import GetCityNum

class Weather:
    t1 = str(round(time.time()))
    headers = {
        'Cookie':f'f_city=%E8%B4%B5%E9%98%B3%7C101260101%7C; vjuids=d7494d7fc.1702d7094f2.0.671014907ea4c; vjlast=1581310318.1581310318.30; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1581310318; cityListHty=101130613%7C101310201%7C101260101%7C101010100%7C101020100%7C101280101%7C101280601%7C101010300; Wa_lvt_51=1581319721; cityListCmp=%E5%8C%97%E4%BA%AC-101010100-20200227%7C%E4%B8%8A%E6%B5%B7-101020100-20200228%7C%E5%B9%BF%E5%B7%9E-101280101-20200229%7C%E6%B7%B1%E5%9C%B3-101280601-20200301%2Cdefault%2C20200227; Wa_lvt_1=1581308047,1581310507,1581430179,1582780936; Wa_lpvt_1={t1}',
        'Host':'d1.weather.com.cn',
        'Referer':'http://www.weather.com.cn/weather1d/101260101.shtml',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    }
    def __init__(self, citi_id='101260101'):
        self.citi_id = citi_id
        pass
    #由城市id获取天气
    def get_weather(self):
        t = str(time.time()).replace('.', '')[:-3]
        id_num = self.get_city_num()
        # url= f'http://d1.weather.com.cn/sk_2d/101260101.html?_={t}'
        url= f'http://d1.weather.com.cn/sk_2d/{id_num}.html?_={t}'
        res=  requests.get(url,headers=self.headers)
        res.encoding=  'utf-8'
        print(res.status_code)
        data = re.search(r'{.+}',res.text)[0]
        data = json.loads(data) 
        '''
        {'nameen': 'guiyang', 'cityname': '贵阳', 'city': '101260101', 'temp': '18', 'tempf': '64', 'WD': '南风', 'wde': 'S', 'WS': '2级', 'wse': '&lt;12km/h', 'SD': '65%', 'time': '16:11', 'weather': '多云', 'weathere': 'Cloudy', 'weathercode': 'd01', 'qy': '876', 'njd': '11.28km', 'sd': '65%', 'rain': '0.0', 'rain24h': '0', 'aqi': '62', 'limitnumber': '不限行', 'aqi_pm25': '62', 'date': '02月27日(星期四)'}
        '''

        print('日期:',data['date'])
        print('城市:',data['cityname'])
        print('限号:',data['limitnumber'])
        print('天气:',data['weather'],data['temp']+'度')
        print('风级:',data['WD'],' level:',data['WS'])

    #由城市id获取周边县区，以及景点,返回json数据
    def get_around_citiy_data(self,citi_id):
        t = str(time.time()).replace('.', '')[:-3]
        url = f'http://d1.weather.com.cn/index_around_2017/{citi_id}.html?_={t}'
        res = requests.get(url,headers=self.headers)
        res.encoding = 'utf-8'
        # print(res.status_code)
        data = re.search(r'{.+}',res.text)[0]
        data = json.loads(data)
        return data


#得到景点,列表
    def get_sight(self):
        id_num = self.get_city_num()
        data = self.get_around_citiy_data(id_num)
        sight_spot = data['jd']#列表
        for each in sight_spot:
            print(each)
        return sight_spot

#得到周边城市
    def get_around(self):
        id_num = self.get_city_num()
        data = self.get_around_citiy_data(id_num)
        around = data['n']
        for each in around:
            print(each)
        return around

#得到当前传说所有社区
    def get_com(self):
        id_num = self.get_city_num()
        data = self.get_around_citiy_data(id_num)
        ser_commu = data['xz']
        for each in ser_commu:
            print(each)
        return ser_commu

    @classmethod
    def get_city_num(cls):
        city = input('查询城市:')
        data = GetCityNum(city)
        id_num,pro_name = data.getrequest()
        print(id_num)
        return id_num

