#!/usr/local/bin/python3
# encoding:utf-8
import requests
import json
from time import sleep
import csv
import random

USER_AGENTS = [
    'MOZILLA/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"
]




def getdata(offset, cookie_num):
    # if offset > 150:
    #     offset = 150
    params = {
        'uuid': '3af152b5c3dc4d05a21f.1585445223.1.0.0',
        'userid': '-1',
        'limit': '50',
        'offset': f'{offset}',
        'cateId': '-1',
        'q': '会所',
    }
    user_agent = random.choice(USER_AGENTS)
    headers = {
        'Cookie': f'uuid=3af152b5c3dc4d05a21f.1585445223.1.0.0; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; _lxsdk_cuid=17123e63dc5c8-0d4447dec4006b-396a7f06-1fa400-17123e63dc5c8;_lxsdk_s=17123e63dc6-04c-414-e9a%7C%7C{str(cookie_num)}',
        'Host': 'apimobile.meituan.com',
        # 'Origin': 'https://zhoushan.meituan.com',
        # 'Referer': 'https://zhoushan.meituan.com/s/%E4%BC%9A%E6%89%80/',
        'Origin': 'https://nn.meituan.com',
        'Referer': 'https://nn.meituan.com/s/%E4%BC%9A%E6%89%80/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': user_agent,
    }
# ci=190; rvct=190;

    res = requests.get(url=url, params=params, headers=headers)

    result = json.loads(res.text)
    data = result['data']
    searchResults = data['searchResult']
    Data = {}
    for each in searchResults:
        Data['title'] = each['title']
        # Data['price'] = each['lowestprice']
        Data['address'] = each['address']
        Data['score'] = each['avgscore']
        Data['cate'] = each['backCateName']
        # Data['area'] = each['city']
        Data['phone'] = each['phone']
        yield Data

url = 'https://apimobile.meituan.com/group/v4/poi/pcsearch/99?'#!GXInanling
# url = 'https://apimobile.meituan.com/group/v4/poi/pcsearch/190?'#!ZHOUSHAN



def main():
    offset = 0
    cookie_num = 92
    headers = ['title','address','score','cate','phone']
    # f = open('play_GUANGXI.csv','w',encoding='utf-8',newline='')
    # writer=  csv.DictWriter(f,headers)
    # writer.writeheader()
    # try:
    while True:
        print('='*100)
        for each in getdata(offset,cookie_num):
            print(each)
            # writer.writerow(each)
        offset += 50
        print('已完成:',offset)
        print('='*100)
        cookie_num += 27
        if offset>1000:
            break
        sleep(1)
    # except Exception as e:
    #     print(e)
    # finally:
    #     f.close()
    #     print('file closed..')


if __name__ == "__main__":
    main()
    
