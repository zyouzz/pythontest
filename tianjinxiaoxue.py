#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

session = requests.session()
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
headers = {'User-Agent': user_agent}
def getpage(url):
    page = session.get(url,headers=headers)
    page.encoding = page.apparent_encoding
    soup = BeautifulSoup(page.text, 'lxml')
    pagedetail=soup.find_all('dl',['left','right'])
    return pagedetail
# def getdetail(urlschool):
#     page1 = session.get(urlschool, headers=headers)
#     page1.encoding = page1.apparent_encoding
#     soup1 = BeautifulSoup(page1.text, 'lxml')
#     title = soup1.find_all('hl', 'nobackground')[0].text
#     detail = soup1.find_all('div', 'detail-xx clearfix')[0].find_all('li')
#     address=detail[0].text
#     phone=detail[1].text
#     youbian = detail[2].text
#     wangzhan = detail[3].text
#     jieshao = soup1.find_all('div', 'detail-xx-jieshao')[0].text
#
#     return title,address,phone,youbian,wangzhan,jieshao
i=0
errorlink=[]
for pn in range(14):
    if pn==0:
        url='http://tianjin.xuexiaodaquan.com/daxue/'
    else:
        url='http://tianjin.xuexiaodaquan.com/daxue/pn'+str(pn+1)+'.html'
    urlstore=getpage(url)
    try:
        for urlde in urlstore:
            urlschool=urlde.find_all('a')[0].get('href')
            print urlschool
            i+=1
            page1 = session.get(urlschool, headers=headers)
            page1.encoding = page1.apparent_encoding
            soup1 = BeautifulSoup(page1.content, 'lxml')
            print soup1
            # print soup1.find_all('hl', 'nobackground')
            title = soup1.find_all('div', 'crumbs')[0].find_all('strong')[0].text
            detail = soup1.find_all('div', 'detail-xx clearfix')[0].find_all('li')
            address = detail[0].text[3:].strip()
            phone = detail[1].text[3:].strip()
            youbian = detail[2].text[3:].strip()
            wangzhan = detail[3].text[3:].strip()
            jieshao = soup1.find_all('div', 'detail-xx-jieshao')[0].text.strip().replace('\r\n','').replace('\n\t','').replace('\n','')
            files = open(r'C:\Users\Esri\Desktop\daxue.txt', 'a+')
            files.write(('%s|%s|%s|%s|%s|%s|%s\n' % (title, address, phone, youbian, wangzhan,urlschool, jieshao)))
    except Exception,e:
        print urlschool + '出错'
        errorlink.append(urlschool)
        print e
        continue
print errorlink
print i


