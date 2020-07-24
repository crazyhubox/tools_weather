#!/usr/local/bin/python3
# encoding:utf-8
from selenium import webdriver
import re
import time
from time import sleep
import requests
from scrapy.selector import Selector
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class QqRoom:
    url = 'https://i.qq.com/'
    my_url = 'https://user.qzone.qq.com/970161120/infocenter'
    def __init__(self):
        option = webdriver.ChromeOptions()
        # prefs = {"profile.managed_default_content_settings.images":2}
        # option.add_experimental_option("prefs",prefs)
        option.add_argument('headless')
        # self.driver = webdriver.Chrome(chrome_options=option)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver,5)
    

    def get_cookies(self):
        try:
            self.driver.get(self.url)
            # self.driver.switchTo
            #切换框架
            self.driver.switch_to.frame('login_frame')
            # 需要实现登录qq
            self.driver.find_element_by_css_selector('#img_out_970161120').click()
            sleep(1)
            self.driver.get(self.my_url)
            try:
                self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.head-info')))
            except:
                pass
            self.driver.find_element_by_css_selector('div.nav-list-inner a').click()

            cookie = {}
            for each in self.driver.get_cookies():
                cookie[each['name']] = each['value']
            return cookie
        except Exception as e:
            self.driver.quit()
            print((e))
        else:
            self.driver.quit()
            print('浏览器退出')


    def publish(self):
        t = time.ctime().split(' ')
        headers = {
            # 'if-modified-since':f'{t[0]}, 29 Feb 2020 {t[3]} GMT',
            'if-modified-since':'Sat, 29 Feb 2020 06:49:35 GMT',
            'sec-fetch-dest':'document',
            'sec-fetch-mode':'navigate',
            'sec-fetch-site':'none',
            'sec-fetch-user':'?1',
            'upgrade-insecure-requests':'1',
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        }

        while True:
            cookies = self.get_cookies()
            if cookies:
                res = requests.get(url=self.my_url,cookies=cookies,params=None,headers=headers)
                print(res.status_code)
                print(res,cookies)
                print(res.text)
                break
            else:
                input('获取cookie失败,重试。。')
                




QqRoom().publish()
