#!/usr/local/bin/python3
# encoding:utf-8
import requests
from urllib.parse import urlencode
import time
import json
import re


class BiLi:
    t = round(time.time())
    headers = {
        'Cookie': "sid=92szinnd; _uuid=DC3A1C73-38F7-1AA8-EDD7-E90560887A2507511infoc; buvid3=D2387481-2523-4AB2-9290-9406AE6D4249155827infoc; CURRENT_FNVAL=16; LIVE_BUVID=AUTO3615806156192857; rpdid=|(J|ulJkYu0J'ul)|YulYkJ; CURRENT_QUALITY=112; DedeUserID=276561775; DedeUserID__ckMd5=e49dc09541af8959; SESSDATA=4fa6280b%2C1584531120%2C5506b321; bili_jct=f43ae4121c4fa909449f6a327adf5757; bp_t_offset_276561775=357938683208439087",
        'Host': 'api.bilibili.com',
        'Referer': 'https://search.bilibili.com/all?keyword=a',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    }
    def search(self):
        page = '1'
        key = input('搜索内容:')
        while True:
            params = {
                'context': '',
                'page': page,
                'order': '',
                'keyword': key,
                'duration': '',
                'tids_1': '',
                'tids_2': '',
                '__refresh__': 'true',
                '__reload__': 'false',
                'highlight': '1',
                'single_column': '0',
                'jsonp': 'jsonp',
                'callback': '__jp0',
            }
            if not key:
                return
            base_url = 'https://api.bilibili.com/x/web-interface/search/all/v2?'
            url = base_url + urlencode(params)
            resp = requests.get(url,headers=self.headers)
            if resp.status_code!=200:
                raise Exception(resp.status_code,'响应错误')
            datas = re.search(r'\((.+)\)',resp.text,re.S)[1]
            ressult = json.loads(datas)
            data = ressult['data']
            data = data['result'][-1]
            data = data['data']
            for each in data:
                print('='*100)
                print(each['id'],each['author'])
                print(each['title'])
                print(each['description'])
                print(each['arcurl'])
                print('='*100)
            num = int(page)
            print(f'当前是第{page}页')
            select = input('上一页/下一页？(1/2)')
            if select == '1':
                if num != 1:
                    num-=1
                    page = str(num)
                else:
                    select = input('已经是第一页了！,下一页?')
                    
            elif select == '2':
                num+=1
                page = str(num)
            else:
                break




            
                
                


