#!/usr/local/bin/python3
# encoding:utf-8
import requests,re,time,json
from scrapy.selector import Selector

url = 'https://kns.cnki.net/kns/brief/brief.aspx?'

page_num = "3"
params = {
    'curpage':page_num,
    'RecordsPerPage':'20',
    'QueryID':'3',
    'ID':'',
    'turnpage':'1',
    'tpagemode':'L',
    'dbPrefix':'SCDB',
    'Fields':'',
    'DisplayMode':'listmode',
    'PageName':'ASP.brief_default_result_aspx',
    'isinEn':'1',
}

headers = {
    'Cookie':'Ecp_ClientId=1200306194103248829; RsPerPage=20; cnkiUserKey=ab03d57b-fde3-fca7-4544-a5f4ec144b9d; Ecp_IpLoginFail=2003121.204.28.92; ASP.NET_SessionId=2h5d0vyywplgpn0zvkkmy254; SID_kns=123122; SID_klogin=125144; SID_crrs=125134; KNS_SortType=; SID_krsnew=125133; _pk_ref=%5B%22%22%2C%22%22%2C1584014448%2C%22https%3A%2F%2Fwww.cnki.net%2F%22%5D; _pk_ses=*; SID_kcms=124109; Ecp_LoginStuts={"IsAutoLogin":false,"UserName":"970161120@qq.com","ShowName":"970161120%40qq.com","UserType":"jf","BUserName":"","BShowName":"","BUserType":"","r":"F8H1ZB"}; LID=WEEvREcwSlJHSldTTEYzU3FBN2wveEZNMnk0L0RsYWtlZjNUNDMvMURwcz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!; SID_kns_new=123107; c_m_LinID=LinID=WEEvREcwSlJHSldTTEYzU3FBN2wveEZNMnk0L0RsYWtlZjNUNDMvMURwcz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&ot=03/12/2020 21:09:27; c_m_expire=2020-03-12 21:09:27',
    'Host':'kns.cnki.net',
    'Referer':'https://kns.cnki.net/kns/brief/brief.aspx?curpage=2&RecordsPerPage=20&QueryID=3&ID=&turnpage=1&tpagemode=L&dbPrefix=SCDB&Fields=&DisplayMode=listmode&PageName=ASP.brief_default_result_aspx&isinEn=1&',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'same-origin',
    'Sec-Fetch-User':'?1',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
}

res=  requests.get(url=url,params=params,headers=headers)
print(res.status_code)
select = Selector(text=res.text)
datas = select.css('[bgcolor]')
for each in datas:
    item = {}
    item['author'] = select.css('')
    item['name'] = select.css('.fz14::text')
    item['time'] = select.css('')
    item['publish'] = select.css('')
    print(item)

