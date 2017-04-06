#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import requests
from bs4 import BeautifulSoup
# import urllib2
import json
file = open('C://Users//Esri//Desktop//webdata.txt', 'a')
line ="编号"+ ',' + "用户名"+ ',' + "威望" + ',' + "积分" + ',' + "赞同" + ',' + "感谢" + ',' + "发问" + ',' + "回复" + ',' + "文章" + ',' + "关注" + ',' + "被关注" + ',' + "关注话题" + ',' +"个人主页" + ',' +"个性主页" + '\n'
# 对象file的write方法将字符串line写入file中.
file = file.write(line)
# html = urllib2.urlopen(r'http://api.douban.com/v2/book/isbn/9787218087351')
with open(r"C:\Users\Esri\Desktop\new 2.json", 'r',encoding='utf-8') as f:
    data = json.load(f)
    print(data)
    i=1
    for place in data:
        print(place)
        print(i)
        print(place['position_name'])
        i+=1
