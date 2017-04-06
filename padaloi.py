#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import urllib
import BeautifulSoup
import re
import datetime
import socket
socket.setdefaulttimeout(30)
header = {'Host': 'cs.lianjia.com','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Connection': 'keep-alive'}
# req = urllib2.Request('http://www.gatherproxy.com/zh/', headers=header)
# con = urllib2.urlopen(req)
# # 对con这个对象调用read()方法，返回的是html页面，也就是有html标签的纯文本
# doc = con.read()
# soup = BeautifulSoup.BeautifulSoup(doc)
# # print soup
# house = soup.findAll('tr', {'type': 'Transparent'})
# print house
req = urllib.urlopen('http://www.baidu.com/',proxies={"http":"http://154.127.52.247:8080"})
# con = urllib2.urlopen(req)
# 对con这个对象调用read()方法，返回的是html页面，也就是有html标签的纯文本
doc = req.read()
soup = BeautifulSoup.BeautifulSoup(doc)
# house = soup.findAll('tr', {'type': 'Transparent'})
print soup