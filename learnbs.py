#!/usr/bin/env python
# -*-coding:utf-8 -*-
#http://www.kuaidaili.com代理IP获取
__author__ = 'jiang'
import requests
from bs4 import BeautifulSoup
import datetime
starttime = datetime.datetime.now()
def getproxiesip():
    iplist = []
    # for pagenum in range(1,page):
    content=open(r'‪C:\Users\Esri\Desktop\qq12.html', 'a',encoding='utf-8').read()
    # print 'http://www.kuaidaili.com/free/inha/'+str(pagenum)+'/'
    # content.encoding = content.apparent_encoding
    bfcontent = BeautifulSoup(content,'html.parser')
    print bfcontent
    for i in range(len(bfcontent.find_all('td',{'data-title':'IP'} ))):
        leixing = bfcontent.find_all('td', {'data-title': '类型'})[0].string.gettext()
        ip=bfcontent.find_all('td',{'data-title':'IP'} )[0].string.gettext()
        port=bfcontent.find_all('td',{'data-title':'PORT'})[0].gettext()
        try:
            dailiip={str(leixing).lower():str(ip)+':'+str(port),}
            session=requests.session()
            response = session.get('http://ip.chinaz.com/getip.aspx', proxies=dailiip, timeout=10)
            print dailiip
            iplist.append(dailiip)
        except Exception, e:
            print e
            continue
    return iplist
if __name__=='__main__':
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    timeout=30
    getproxiesip()
endtime = datetime.datetime.now()
print (endtime - starttime).seconds
