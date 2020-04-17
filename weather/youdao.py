#!/usr/local/bin/python3
# encoding:utf-8


import requests
import re
import time
import json
from random import randint
import hashlib
 



# url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'


# t = str(time.time()).replace('.', '')[:-3]
# headers = {
#     'Cookie':f'OUTFOX_SEARCH_USER_ID=-537367871@1.204.33.201; OUTFOX_SEARCH_USER_ID_NCOO=1789273676.6063836; _ntes_nnid=b39d803da9e3681defa5966ce2efab4d,1582514300906; JSESSIONID=aaa1xUfvorprw72fLGOcx; ___rl__test__cookies={t}',
#     'Host':'fanyi.youdao.com',
#     'Origin':'http://fanyi.youdao.com',
#     'Referer':'http://fanyi.youdao.com/',
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
#     'X-Requested-With':'XMLHttpRequest',
# }

# key = 'apple'

# randon_num = str(randint(1,9))
# ts = str(time.time()).replace('.', '')[:-3]
# salt = ts + randon_num
# value = "fanyideskweb" + key + salt + "Nw(nmmbP%A-r6U3EUn]Aj"
# sign = hex5(value)

# datas = {
#     'i':key,
#     'from':'AUTO',
#     'to':'AUTO',
#     'smartresult':'dict',
#     'client':'fanyideskweb',
#     'salt':salt,
#     'sign':sign,
#     'ts':ts,
#     'bv':'85d772a06741ae9950b2a7b061f7e4a4',
#     'doctype':'json',
#     'version':'2.1',
#     'keyfrom':'fanyi.web',
#     'action':'FY_BY_REALTlME',
# }

# res = requests.post(url=url,data=datas,params=None,headers=headers)
# print(res.status_code)
# print(res.text)


class YouDaoTranslate:
    translate_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'



    def translate(self):


        t = str(time.time()).replace('.', '')[:-3]
        headers = {
            'Cookie':f'OUTFOX_SEARCH_USER_ID=-537367871@1.204.33.201; OUTFOX_SEARCH_USER_ID_NCOO=1789273676.6063836; _ntes_nnid=b39d803da9e3681defa5966ce2efab4d,1582514300906; JSESSIONID=aaa1xUfvorprw72fLGOcx; ___rl__test__cookies={t}',
            'Host':'fanyi.youdao.com',
            'Origin':'http://fanyi.youdao.com',
            'Referer':'http://fanyi.youdao.com/',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest',
        }

        key = input('想翻译什么?')
        randon_num = str(randint(1,9))
        ts = str(time.time()).replace('.', '')[:-3]
        salt = ts + randon_num
        value = "fanyideskweb" + key + salt + "Nw(nmmbP%A-r6U3EUn]Aj"
        sign = self.hex5(value)

        datas = {
            'i':key,
            'from':'AUTO',
            'to':'AUTO',
            'smartresult':'dict',
            'client':'fanyideskweb',
            'salt':salt,
            'sign':sign,
            'ts':ts,
            'bv':'85d772a06741ae9950b2a7b061f7e4a4',
            'doctype':'json',
            'version':'2.1',
            'keyfrom':'fanyi.web',
            'action':'FY_BY_REALTlME',
        }
        res = requests.post(url=self.translate_url,data=datas,params=None,headers=headers)
        data = json.loads(res.text)
        print('翻译内容为:',key)
        print('翻译结果为:\n',data['translateResult'])
        print(data['smartResult']['entries'])   

    



    def hex5(self,value):
        manipulator = hashlib.md5()
        manipulator.update(value.encode('utf-8'))
        return manipulator.hexdigest()



# YouDaoTranslate().translate()