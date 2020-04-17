#!/usr/local/bin/python3
# encoding:utf-8
from weather.WeClass import Weather
from weather.GetCityNum import GetCityNum
from weather.sight_pro import GetSight_province
from weather.BILIsearch import BiLi
from weather.meituan import Meituan
from weather.youdao import YouDaoTranslate

def main():
    while True:
        try:
            run()
        except Exception as e:
            if str(e) == '0':
                return
            print(e)    
            print('='*100)
            continue

        
def run():
    select = input('''请选择功能(1-4):
1.查询天气情况      10.翻译      
2.查询周边景点             
3.查询当地社区          
4.查询周边城市            
5.查询省3A景区
6.一言
7.B站逛一下
8.上美团搜酒店
9.上美团搜娱乐/美食
0.退出
'''
)
    if select == '0':
        raise Exception('0')
    wther = Weather()
    Mt = Meituan()
    pro_sight = GetSight_province()
    switcher = {
        '1':wther.get_weather,
        '2':wther.get_sight,
        '3':wther.get_com,
        '4':wther.get_around,
        '5':pro_sight.getSight,
        '6':GetCityNum.encourage,
        '7':BiLi().search,
        '8':Mt.search_Hotel,
        '9':Mt.search_NotHotel,
        '10':YouDaoTranslate().translate
    }
    print('='*100)
    switcher[select]()
    input('='*100)





if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
