#!/usr/bin/env python
# -*-coding:utf-8 -*-
# # # listn=[n for n in range(10)]
# # # print listn
# # print range(1,3)
# def fenreneu(changdu,jiange):
#     li=[]
#
#     for newj in range(1,changdu+1,jiange):
#         li.append(range(changdu)[newj:newj+jiange])
#     return li
# print fenreneu(20,3)
# import time
# print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
hbpage=requests.get('https://i.qunar.com/',headers=headers).text
if  BeautifulSoup(hbpage, 'lxml').select('p[class="msg2"]'):
    print 'wucihang'
else:
    try:
        BeautifulSoup(hbpage, 'lxml').select('span[class="title"]')[1]
        print BeautifulSoup(hbpage, 'lxml').select('span[class="title"]')
        print '有'
    except:
        print '网页有错误'