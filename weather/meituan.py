#!/usr/local/bin/python3
# encoding:utf-8
import requests
import re
import time
from scrapy.selector import Selector
from selenium import webdriver
from urllib.parse import urljoin

# some = sele.css('#react').get()
        

class Meituan:
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    city_url = 'https://www.meituan.com/changecity/'
    
    def __init__(self):
        self.driver = webdriver.Chrome(options=self.option)
        self.driver.implicitly_wait(5)
    
    def enter_city(self):
        name = input('哪个城市兄弟:')
        self.driver.get(self.city_url)
        res_city_text = self.driver.page_source
        self.driver.find_element_by_class_name("cities")
        sele = Selector(text=res_city_text)
        link_cities = sele.css('.link.city')
        for each in link_cities:
            city_name = each.css('::text').get()
            url = each.css('::attr(href)').get()
            #查找名字这里需要优化
            if city_name == name:
                return url
    
    
    # 查找酒店
    def search_Hotel(self):
        try:
            base_url = self.enter_city()
            name=  '酒店'
            url_0 = f'/s/{name}/'
            url = 'https:'+urljoin(base_url,url_0)
            print(url)
            self.driver.get(url)
            while True:
                html = self.driver.page_source
                self.driver.find_element_by_class_name('common-list-main')#等到页面加载
                self.anly_hotel(html)
                next_page = input('是否上一页/下一页?(1/2)')
                if next_page=='2':
                    self.driver.find_element_by_css_selector('.right-arrow.iconfont.icon-btn_right').click()
                elif next_page=='1':
                    self.driver.find_element_by_css_selector('.left-arrow.iconfont.icon-btn_left').click()
                else:
                    break
        except Exception as e:
            print(e)
            print('浏览器退出。。。。。。')
            self.driver.quit()
        else:
            print('浏览器退出=========')
            self.driver.quit()
    
    
    # 查找非酒店
    def search_NotHotel(self):
        try:
            base_url = self.enter_city()
            name=  input('哥们,要找什么?')
            url_0 = f'/s/{name}/'
            url = 'https:'+urljoin(base_url,url_0)
            print(url)
            self.driver.get(url)
            while True:
                html = self.driver.page_source
                self.driver.find_element_by_class_name('common-list-main')#等到页面加载
                self.anly_nothotel(html)
                next_page = input('是否上一页/下一页?(1/2)')
                if next_page=='2':
                    self.driver.find_element_by_css_selector('.right-arrow.iconfont.icon-btn_right').click()
                elif next_page=='1':
                    self.driver.find_element_by_css_selector('.left-arrow.iconfont.icon-btn_left').click()
                else:
                    break
        except Exception as e:
            print(e)
            print('浏览器退出。。。。。。')
            self.driver.quit()
        else:
            print('浏览器退出=========')
            self.driver.quit()
       

    #分析非酒店
    def anly_nothotel(self,html):
        sele = Selector(text=html)
        results = sele.css('.default-list-item.clearfix')
        for each in results:
            print('='*100)
            url = each.css('a::attr(href)').get()
            name = each.css('.list-item-desc-top a::text').get()
            review = each.css('.item-eval-info.clearfix span::text').getall()
            category = each.css('.cate-info.ellipsis span::attr(title)').getall()
            price_for_each = each.css('.avg-price::text').getall()
            discount = each.css('.deal-title a')
            print('https:'+url)
            print(name)
            print((review))
            print(category)
            if price_for_each:
                print(price_for_each)
            else:
                print('暂无价格')
            for each in discount:
                info_ = each.css('span').getall()
                print(info_)
            print('='*100)

    #分析酒店
    def anly_hotel(self,html):
        sele = Selector(text=html)
        results = sele.css('.common-list-main [data-poiid]')
        for each in results:
            url = each.css('a::attr(href)').get()
            name = each.css('.list-item-desc-top a::text').get()
            review = each.css('.item-eval-info.clearfix span::text').getall()
            category = each.css('.cate-info.ellipsis span::attr(title)').getall()
            price_for_each = each.css('.avg-price::text').getall()
            discount = each.css('.deal-title a')
            print('https:'+url)
            print(name)
            print((review))
            print(category)
            if price_for_each:
                print(price_for_each)
            else:
                print('暂无价格')
            for each in discount:
                info_ = each.css('span').getall()
                print(info_)
            print('='*100)
        pass


