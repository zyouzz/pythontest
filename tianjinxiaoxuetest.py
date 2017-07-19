#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
from bs4 import BeautifulSoup
import requests
session = requests.session()
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
headers = {'User-Agent': user_agent}
urlschool='http://tianjin.xuexiaodaquan.com/xuexiao/408061.html'
page1 = session.get(urlschool,headers=headers)

page1.encoding = page1.apparent_encoding
soup1 = BeautifulSoup(page1.content,"lxml")
# jinwei=str(soup1).split('.Point(')[1].split(');')[0]
ieshao = soup1.find_all('div', 'detail-xx-jieshao')[0].text.strip().replace('\r\n','').replace('\n\t','').replace('\n','')
print ieshao

# jieshao = soup1.find_all('div', 'detail-xx-jieshao')[0].text.strip().replace('\r\n','').replace('\n\t','')
# title = soup1.find_all('div', 'crumbs')[0].find_all('strong')[0].text
# detail = soup1.find_all('div', 'detail-xx clearfix')[0].find_all('li')
# address = detail[0].text[3:].strip()
# phone = detail[1].text[3:].strip()
# youbian = detail[2].text[3:].strip()
# print soup1
