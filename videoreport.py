#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import requests
from bs4 import BeautifulSoup

##优酷
# def getyouku(urlmain,urlvideo):
#     headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
#     pagemain = requests.get(urlmain, headers=headers).text
#     totalview = int(BeautifulSoup(pagemain, 'lxml').find_all('li', "vnum")[0].get('title').replace(',',''))
#     totalfans = int(BeautifulSoup(pagemain, 'lxml').find_all('li', "snum")[0].get('title').replace(',',''))
#     pagevideo = requests.get(urlvideo, headers=headers).text
#     totalvideo = int(BeautifulSoup(pagevideo, 'lxml').find_all('div', "title")[0].text.split('(')[1].replace(')','').replace(',',''))
#     return totalview,totalfans,totalvideo
#
# ##ArcGIS培训视频中心 优酷
# peixun=getyouku('http://i.youku.com/arcgis','http://i.youku.com/i/UNDExNTE4NjM3Mg==/videos')
#
# ##esrichina 优酷
# esriy=getyouku('http://i.youku.com/esrichina','http://i.youku.com/i/UODU1ODAyODg=/videos')
# #
# # #
# print peixun,esriy
#
# ##腾讯
def gettengxun(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    page = requests.get(url, headers=headers).text
    totalview2 = float(BeautifulSoup(page, 'lxml').find_all('span', "count_num")[2].text[:-3])*10000
    totalfans2 = int(BeautifulSoup(page, 'lxml').find_all('span', "count_num j_rss_count")[0].text)
    totalvideo2 = int(BeautifulSoup(page, 'lxml').find_all('span', "count_num")[0].text)
    return int(totalview2),totalfans2,totalvideo2

##ArcGIS微助手 tengxun
weizhushou=gettengxun('http://v.qq.com/vplus/b7a560095d71f2524037313facdf59e3')

##Esrichina
esrit=gettengxun('http://v.qq.com/vplus/f05bbaee87fc9708abe3c6c6aff3832c')

print weizhushou,esrit
#
# ##ArcGIS产品与技术专栏
# def getchanpin(url):
#     headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
#     title=[]
#     titlelink=[]
#     view=[]
#     for pagenum in range(1,40):
#         print '-----开始爬第%d页-----'%pagenum
#         page = requests.get(url+'/%s'%pagenum, headers=headers).text
#         title1 = BeautifulSoup(page, 'lxml').find_all('span', "link_title")
#         titlelink1 = BeautifulSoup(page, 'lxml').select('h1 > span > a')
#         view1 = BeautifulSoup(page, 'lxml').find_all('span', "link_view")
#         title3=[]
#         titlelink3=[]
#         view3=[]
#         for (title2,view2,titlelink2) in zip(title1,view1,titlelink1):
#             title3.append(title2.text.replace('        ','').replace('\n','').replace('    \r',''))
#             titlelink3.append('http://blog.csdn.net/'+titlelink2.get('href'))
#             view3.append(view2.text.split('(')[1].replace(')',''))
#         title.extend(title3)
#         titlelink.extend(titlelink3)
#         view.extend(view3)
#
#
#     return title,view,titlelink
#
# ##ArcGIS产品与技术专栏
# arcgisproduction=getchanpin('http://blog.csdn.net/arcgis_all/article/list')
# # print arcgisproduction[0]
# files = open(r'C:\Users\Esri\Desktop\arcgischanpin.txt', 'a+')
# for i in  range(len(arcgisproduction[0])):
#     files.write(('%s,%s,%s'%(arcgisproduction[0][i],arcgisproduction[1][i],arcgisproduction[2][i])).encode('utf-8'))

