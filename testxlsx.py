#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import xlsxwriter
from bs4 import BeautifulSoup
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')
session = requests.session()
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
headers = {'User-Agent': user_agent}
link="http://resources.arcgis.com/zh-cn/help/main/10.2/00w0/00w000000009090142.htm"
page = session.get(link, headers=headers)
page.encoding = page.apparent_encoding
soup = BeautifulSoup(page.text, 'lxml')
title1=soup.title.text[19:] #题目
dec=soup.find_all('div', 'gpmsg_desc')[0].text #描述
if len(soup.find_all('div','gpmsg_soln'))==0:
    sol = '暂无解决方案'
else:
    print soup.find_all('div','gpmsg_soln')[0].find_all('a')
    if len(soup.find_all('div','gpmsg_soln')[0].find_all('a'))==0:
        soltem1=soup.find_all('div','gpmsg_soln')[0].text  #解决方案
    else:
        if len(soup.find_all('div','gpmsg_soln')[0].find_all('p'))==1:
            soltem1=soup.find_all('div','gpmsg_soln')[0].text
            for lli in soup.find_all('div','gpmsg_soln')[0].find_all('a'):
                dizhi='http://resources.arcgis.com'+lli.get('href')
                dtext=lli.text
                newdtext='[url=%s]%s[/url]'%(dizhi,dtext)
                soltem1=soltem1.replace(dtext,newdtext)
        else:
            soltem1 = ' '
            print len(soup.find_all('div','gpmsg_soln')[0].find_all('p'))
            for num in range(len(soup.find_all('div','gpmsg_soln')[0].find_all('p'))):
                tempp =soup.find_all('div','gpmsg_soln')[0].find_all('p')[num].text
                print tempp
                if len(soup.find_all('div', 'gpmsg_soln')[0].find_all('p')[num].find_all('a'))==0:
                    if num==0:
                        soltem1 = tempp
                    else:
                        soltem1 = soltem1 + '\n' + tempp
                else:
                    for lli in soup.find_all('div', 'gpmsg_soln')[0].find_all('p')[num].find_all('a'):
                        dizhi = 'http://resources.arcgis.com' + lli.get('href')
                        dtext = lli.text
                        newdtext = '[url=%s]%s[/url]' % (dizhi, dtext)
                        if num==0:
                            soltem1=tempp.replace(dtext, newdtext)
                        else:
                            soltem1 = soltem1 + '\n' + tempp.replace(dtext, newdtext)
vvv=title1.encode("utf-8")
ss='aaaa'
print type(ss)
print type(vvv)
ff=open(r'C:\Users\Esri\Desktop\solution66.txt','a+')
ff.write(vvv.strip('\n'))
print vvv.replace('\r\n',' ')

# print soltem1+'\n'+'[b][url=%s]%s[/url][/b]]'%(link,link)
aaaa='[b]【解决方案】[/b]'+'\n'+soltem1+'\n'+'\n'+'[b]【原文链接】[/b]'+'\n'+'[b][url=%s]%s[/url][/b]'%(link,link)
# print soup.prettify()

workbook = xlsxwriter.Workbook('hello.xlsx') # 建立文件

worksheet = workbook.add_worksheet() # 建立sheet， 可以work.add_worksheet('employee')来指定sheet名，但中文名会报UnicodeDecodeErro的错误

worksheet.write('A1', aaaa) # 向A1写入
#
workbook.close()