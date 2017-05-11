#!/usr/bin/env python
# -*-coding:utf-8 -*-
#__author__ = 'jiang'
from selenium import  webdriver
from multiprocessing import Pool
from bs4 import BeautifulSoup
import requests
import time
def getip(url,processi):
    # iplist=[]
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print '进程%s开始'%processi
    print url
    for pa in url:
        try:
            driver=webdriver.PhantomJS(executable_path=r"D:\Python27\phantomjs-2.1.1-windows\bin\phantomjs")
            link='http://support.esri.com/technical-article/0000'+str(pa+12719)
            driver.get(link)
            # print driver.page_source
            # time.sleep(15)
            print 'http://support.esri.com/technical-article/0000'+str(pa+12719)
            bfcontent=BeautifulSoup(driver.page_source,'lxml')
            driver.close()
            ids=pa+12719
            ss=open('C:\Users\Esri\Desktop\%d.txt'%ids,'w')
            ss.write(bfcontent.encode('utf-8'))
            ss.close()
        except Exception,e:
            print e
            continue
        # print '>>>>>正在爬取第%d页>>>>>'%pa
        # for i in range(len(bfcontent.find_all('td', {'data-title': 'IP'}))):
        #     leixing = bfcontent.find_all('td', {'data-title': '类型'})[0].string.gettext()
        #     ip = bfcontent.find_all('td', {'data-title': 'IP'})[0].string.gettext()
        #     port = bfcontent.find_all('td', {'data-title': 'PORT'})[0].gettext()
        #     dailiip = {str(leixing).lower(): str(ip) + ':' + str(port), }
        #     iplist.append(dailiip)
        #     print iplist
        # iplist.append(url)
    # return iplist
def fenreneu(changdu,jiange):
    li=[]
    for newj in range(1,changdu+1,jiange):
        li.append(range(changdu)[newj:newj+jiange])
    return li
if __name__=='__main__':
    fin_save_list = []
    p = Pool(5)  # 设置进程池
    # result = []
    url=fenreneu(5,1)# 多进程结果列表
    for i in range(len(url)):
        p.apply_async(getip, args=(url[i],i))
        # print result
    p.close()
    p.join()
    # for result_i in range(len(result)):
    #     fin_info_result_list = result[result_i].get()
    #     fin_save_list.extend(fin_info_result_list)  # 将各个进程获得的列表合并
    # print result