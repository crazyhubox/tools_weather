#!/usr/local/bin/python3
# encoding:utf-8


import requests
import json
import time
from urllib.parse import urlencode
import other_tools.getsign as GS

# *百度翻译_单词
class BaiduTranslation:
    headers = {
        'cookie': 'BAIDUID=0CBFF0AE063CAF967683508539B12C04:FG=1; BDUSS=o3VnBmU21DUnFTd3pocHZ1SXp3dFJ-VEtqY2l6U3V1amtWREhtLX5aalI2SjllRVFBQUFBJCQAAAAAAAAAAAEAAABPy-9AaGloTGlicmEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANFbeF7RW3heSH; cflag=13%3A3; session_name=cn.bing.com; session_id=1585122262135; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1585144011; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1585144011; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; yjs_js_security_passport=7a2a5dde5dec1332f80a47360df9b4ddcd614421_1585144011_js; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
        'origin': 'https://fanyi.baidu.com',
        'referer': 'https://fanyi.baidu.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36 Edg/80.0.361.69',
        'x-requested-with': 'XMLHttpRequest',
    }


    def word_translate(self,key):
        """translate for a word,en->ch or ch->en;

        Arguments:
            key {str} -- 一个字符串 
        """
        url = 'https://fanyi.baidu.com/sug'
        datas = {
            'kw': key,
        }
        res = requests.post(url=url, data=datas)
        result = json.loads(res.text)
        data = result['data']
        for each in data:
            print(each)


    def words_translate(self):
        SELECT_DICT = {
            '1': {
                'from': 'en',
                'to': 'zh',
            },
            '2': {
                'from': 'zh',
                'to': 'en',
            }
        }
        selection = input('Which kind of translation?[ 1,(en->zh) / 2,zh->en)]')
        url = 'https://fanyi.baidu.com/v2transapi?'
        url = url+urlencode(SELECT_DICT[selection])
        key = input('The word:')
        sign = GS.get_sign(key)
        datas = {
            'query': key,
            'transtype': 'realtime',
            'simple_means_flag': '3',
            'sign': sign,
            'token': 'cc68b5cef35254f04ed28b496982fdfd',
            'domain': 'common',
        }

        res = requests.post(url=url, data=datas,headers=self.headers)  
        html =res.text
        self.format_data(html)
        

    def format_data(self,html:str):
        result = json.loads(html)
        trans_result = result['trans_result']
        dict_result  = result['dict_result']
        liju_result = result['liju_result']


        #*简单的使用情况
        print('='*50+'简单的使用情况'+'='*50)
        means = dict_result['simple_means']['word_means']
        print(means)
        print('='*50+'例子'+'='*50)
        #*使用情景
        try:
            UseCase1 = dict_result['usecase']['collocation']['data'][0]['ex']
            UseCase2 = dict_result['usecase']['collocation']['data'][0]['ex']
            for each in UseCase1:
                print(each)
            for each in UseCase2:
                print(each)
        except:
            pass
        print('='*50+'同义词'+'='*50)
        #*同义词
        try:
            sanyms = dict_result['sanyms'][0]['data']
            for each in sanyms:
                print(each)
        except:
            pass
        print('='*50+'反义词'+'='*50)
        #*反义词
        try:
            antonyms = dict_result['sanyms'][1]['data']
            for each in antonyms:
                print(each)
        except:
            pass
        print('='*100)


