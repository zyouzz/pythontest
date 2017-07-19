#!/usr/bin/env python
# -*-coding:utf-8 -*-
#-*-coding:utf-8 -*-
__author__ = 'Jy2881'

from bs4 import BeautifulSoup
from selenium import webdriver
import re,os,multiprocessing
from multiprocessing import queues,Process,Manager

# user_list = [11282, 27857, 58568]
# 61300
user_list = []

driver = webdriver.PhantomJS(executable_path=r"D:\Python27\phantomjs-2.1.1-windows\bin\phantomjs.exe")

def make_user_list(url,url_new,i):
    print(url_new)
    driver.get(url_new)
    html = driver.page_source

    bsObj = BeautifulSoup(html,"lxml")
    for link in bsObj.findAll("div",class_="booklist-item"):
        print link.findAll("div",class_="title")[0].findAll("a")[0].get_text()
        # if link.findAll("div",class_="title")[0].findAll("a")[0].get_text() =="巫师世界".encode('utf-8'):
        return url_new

    if bsObj.findAll("a",class_="btn btn-primary btn-block"):
        for button in bsObj.findAll("a",class_="btn btn-primary btn-block"):
            if button.get_text() == "点击加载下一页":
                str = button.get("onclick")
                print(str)
                number = re.findall(r'[^()]+',str)[1][5:-1]
                url_new = url+"?t=%s"%number
                return make_user_list(url,url_new,i)
    print('Sub process %s.' % os.getpid())
    driver.close()
def myCallBack(args):
    global user_list
    if args != None:
        user_list.append(args)

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = multiprocessing.Pool(8)
    for i in range(621880,621895):
        url = "http://www.yousuu.com/user/%d/comments"%i
        url_new = url
        p.apply_async(make_user_list, args=(url,url_new,i),callback=myCallBack)
    p.close()
    p.join()

    print(user_list)
