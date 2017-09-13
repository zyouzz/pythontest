#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def get_page(url):
    print(url)
    driver = webdriver.PhantomJS(executable_path=r'D:\Python27\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    driver.get(url)
    data = driver.page_source
    driver.close()
    bfcontent = BeautifulSoup(data,  "html.parser")
    print bfcontent.find_all('div',id='sina_keyword_ad_area2')[0].find_all('p')
def get_url(mainpage):
    print(mainpage)
    driver = webdriver.PhantomJS(executable_path=r'D:\Python27\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    driver.get(mainpage)
    data = driver.page_source
    driver.close()
    listcontent = BeautifulSoup(data, "html.parser")
    return listcontent.find_all('div','articleList')[0].find_all('div','articleCell SG_j_linedot1')

# get_page("http://blog.sina.com.cn/s/blog_764b1e9d0102xdfj.html")
# get_url('http://blog.sina.com.cn/s/articlelist_1984634525_0_1.html')
for numpage in range(1,3):
    mainpage="http://blog.sina.com.cn/s/articlelist_1984634525_0_"+str(numpage)+".html"
    for murl in get_url(mainpage):
        print murl.find_all("a")[0].get("href")
