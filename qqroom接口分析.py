#!/usr/local/bin/python3
# encoding:utf-8

import re
import requests
import json
import time
import hashlib
from scrapy import Selector
from urllib.parse import urlencode
import asyncio

t = str(round(time.time()))
url_index = 'https://user.qzone.qq.com/proxy/domain/qzonestyle.gtimg.cn/qzone/hybrid/lib/pow/worker/index.js'
headers_index = {
    'Referer':'https://user.qzone.qq.com/proxy/domain/qzonestyle.gtimg.cn/qzone/hybrid/lib/pow/worker/pow.js',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
}

res_index = requests.get(url_index,headers=headers_index)
result = res_index.headers
data = result['x-stgw-ssl-info']
ssl_info = data[:-1]+'h2|0'


headers = {
    'cookie':f'x-stgw-ssl-info={ssl_info};',
    'if-modified-since':'Wed, 26 Feb 2020 05:19:07 GMT',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'none',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
}
# url_room = 'https://user.qzone.qq.com/970161120/infocenter'
# res_login = requests.get(url_room,headers=headers)

def publish(key_word):
    # key_word  = 'this is python'

    params = {
        'qzonetoken':'bb0889e53a0decaf70bd3354900a21c33169c9f3610ef4cdfdd7a4b597cb06a578b486911ddda6',
        'g_tk':'1078213508',
    }
    datas = {
        'syn_tweet_verson':'1',
        'paramstr':'1',
        'pic_template':'',
        'richtype':'',
        'richval':'',
        'special_url':'',
        'subrichtype':'',
        'who':'1',
        'con':f'qm{key_word}',
        'feedversion':'1',
        'ver':'1',
        'ugc_right':'1',
        'to_sign':'1',
        'hostuin':'970161120',
        'code_version':'1',
        'format':'fs',
        'qzreferrer':'https://user.qzone.qq.com/970161120/infocenter?via=toolbar',
    }
    url_post = 'https://user.qzone.qq.com/proxy/domain/taotao.qzone.qq.com/cgi-bin/emotion_cgi_publish_v6?'
    url_post =url_post + urlencode(params)
    res = requests.post(url_post,data=datas,headers=headers)
    print(res.status_code)
    if res.status_code==200:
        print(key_word,'is ok',res.text)


res = requests.get(url='https://user.qzone.qq.com/970161120/infocenter',params=None,headers=headers)

print(res.text)