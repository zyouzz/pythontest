#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import requests
from bs4 import BeautifulSoup
url='http://support.esri.com/Products/Desktop/arcgis-desktop/arcmap/10-5'
headers={'Host': 'support.esri.com','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
post_data = {'ItemGUID':'e8294afe-faf5-4ede-9f9a-90b3fb8db6e6'}
page=requests.post(url,headers=headers,data=post_data)
# page.encoding = page.apparent_encoding
# soup = BeautifulSoup(page.text, 'lxml')
print page.text