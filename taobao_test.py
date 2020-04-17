#!/usr/local/bin/python3
# encoding:utf-8
from selenium import webdriver
import time
from scrapy.selector import Selector


def get_category():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    url = 'https://s.taobao.com/search?q=%E5%AF%B9%E6%88%92'
    driver.get(url=url)
    time.sleep(15)
    button = driver.find_element_by_css_selector('.item.next')
    while button:
        button.click()
        time.sleep(5)
        button = driver.find_element_by_css_selector('.item.next')
        html = driver.page_source
        sele = Selector(text=html)
        cate = sele.css('[data-category]')
        yield cate

    print("发生错误")
    driver.quit()


def main():
    for category in get_category():
        for each in category:
            price = each.css(
                '.price.g_price.g_price-highlight span::text,.price.g_price.g_price-highlight strong::text').getall()
            price = ''.join(price)
            print(price)
    pass


if __name__ == "__main__":
    main()
    
