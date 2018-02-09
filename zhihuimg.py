#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
from bs4 import BeautifulSoup
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')
session = requests.session()
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
headers = {'User-Agent': user_agent}
def getimg(url):
    page = session.get(url,headers=headers)
    page.encoding = page.apparent_encoding
    pagedetail = BeautifulSoup(page.text, 'lxml')
    return pagedetail
def dowloadimg(imageUrl,filePath):
    r = requests.get(imageUrl)
    print filePath
    with open(filePath, "wb") as code:
        code.write(r.content)
for pageno in range(9):
    url="http://zhihu.esrichina.com.cn/question/id-19341__sort-DESC__page-"+str(pageno+1)
    redetail=getimg(url)
    ree=redetail.find_all('div',"aw-item")[1:]
    for dure in ree:
        name = dure.find_all('a', "aw-user-name")[0].text
        huitime =dure.find_all('span', "text-color-999 pull-right")[0].text[5:]
        if dure.find_all('div',"aw-upload-img-list"):
            paath='c:/Users/Esri/Desktop/zhihuimg/' + name
            img = dure.find_all('div', "aw-upload-img-list")
            for pinci in img:
                if pinci.find_all('a'):
                    n=1
                    for ii in pinci.find_all('a'):
                        print name
                        print huitime
                        imgurl=ii.get('href')
                        print imgurl
                        paath1=paath+str(n)+"."+imgurl.split('.')[-1]
                        dowloadimg(imgurl, paath1)
                        filezh=open(r'c:/Users/Esri/Desktop/zhihuimg/zhihu.txt','a+')
                        filezh.write('{},{},{},{}\n'.format(name,huitime,imgurl,url))
                        n+=1



