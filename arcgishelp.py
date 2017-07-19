#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import json
import xlsxwriter
import sys
reload(sys)
sys.setdefaultencoding('utf8')

session = requests.session()
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
headers = {'User-Agent': user_agent}
# page = session.get("http://resources.arcgis.com/zh-cn/help/main/10.2/00vp/00vp0000001q000078.htm", headers=headers)
# page.encoding = page.apparent_encoding
# soup = BeautifulSoup(page.text, 'lxml')
# print soup.prettify()
# driver = webdriver.PhantomJS(executable_path=r'D:\Python27\phantomjs-2.1.1-windows\bin\phantomjs.exe')
# driver.get("http://resources.arcgis.com/zh-cn/help/main/10.2/00vp/00vp00000009000038.htm")
# data = driver.page_source
# # print(data)
# driver.close()
# bfcontent = BeautifulSoup(data, 'lxml')
# print bfcontent
folder='C:\Users\Esri\Desktop\json'
folder1='C:\Users\Esri\Desktop'
xlsx11=os.path.join(folder1, "solution99.xlsx")
print xlsx11
excx = xlsxwriter.Workbook(xlsx11)
worksheet = excx.add_worksheet()
# worksheet.write(1,2,'aa')
# excx.close()
# print excx
filename=os.listdir(folder)
i = -1
row = 0
errorr=[]
folder2='C:/Users/Esri/Desktop/json/'
for name in range(1,11):
    jsonpath=folder2+str(name)+'.json'
    print jsonpath
# jsonpath=r'C:\Users\Esri\Desktop\json\9.json'
    with open(jsonpath) as json_file:
        data = json.load(json_file)
        # link='http://resources.arcgis.com/zh-cn/help/main/10.2/'+
        firsl=data['tree'][data["rootElement"]]["c"]

        for first in firsl:
            # if i==140:
            #     break
            second2=data['tree'][first]["c"]
            for se in second2:
                third3=data['tree'][se]
                link='http://resources.arcgis.com/zh-cn/help/main/10.2/'+se[:4]+'/'+se+'.htm'
                print link
                print i
                i+=1
                # if i==140:
                #     break
                page = session.get(link,headers=headers)
                page.encoding = page.apparent_encoding
                soup = BeautifulSoup(page.text, 'lxml')
                # print soup.prettify()
                try:
                    title='【Desktop】工具错误码-'+soup.title.text[19:].replace('\r\n',' ') #题目
                    if len(soup.find_all('div', 'gpmsg_desc'))==0:
                        decc='无描述'
                    else:
                        decc = ' '
                        # print len(soup.find_all('div', 'gpmsg_desc')[0].find_all('p'))
                        for num1 in range(len(soup.find_all('div', 'gpmsg_desc')[0].find_all('p'))):
                            tempp1 = soup.find_all('div', 'gpmsg_desc')[0].find_all('p')[num1].text.replace('\r\n',' ')
                            # print tempp1
                            if len(soup.find_all('div', 'gpmsg_desc')[0].find_all('p')[num1].find_all('a')) == 0:
                                if num1 == 0:
                                    decc = tempp1
                                else:
                                    decc = decc + '\n' + tempp1
                            else:
                                for lli in soup.find_all('div', 'gpmsg_desc')[0].find_all('p')[num1].find_all('a'):
                                    dizhi1 = 'http://resources.arcgis.com' + lli.get('href')
                                    dtext = lli.text
                                    newdtext1 = '[url=%s]%s[/url]' % (dizhi1, dtext)
                                    if num1 == 0:
                                        decc = tempp1.replace(dtext, newdtext1)
                                    else:
                                        decc = decc + '\n' + tempp1.replace(dtext, newdtext1)
                        # if len(soup.find_all('div', 'gpmsg_desc')[0].find_all('a')) == 0:
                        #     dec = soup.find_all('div', 'gpmsg_desc')[0].text  # 描述
                        # else:
                        #     dec = soup.find_all('div', 'gpmsg_desc')[0].text
                        #     for lli1 in soup.find_all('div', 'gpmsg_desc')[0].find_all('a'):
                        #         dizhi1 = 'http://resources.arcgis.com' + lli1.get('href')
                        #         dtext1 = lli1.text
                        #         newdtext1 = '[url=%s]%s[/url]' % (dizhi1, dtext1)
                        #         dec = dec.replace(dtext1, newdtext1)
                    if len(soup.find_all('div','gpmsg_soln'))==0:
                        soltem1 = '见描述或者无需解决方案'
                    else:
                        soltem1 = ' '
                        # print len(soup.find_all('div', 'gpmsg_soln')[0].find_all('p'))
                        for num in range(len(soup.find_all('div', 'gpmsg_soln')[0].find_all('p'))):
                            tempp = soup.find_all('div', 'gpmsg_soln')[0].find_all('p')[num].text.replace('\r\n',' ')
                            # print tempp
                            if len(soup.find_all('div', 'gpmsg_soln')[0].find_all('p')[num].find_all('a')) == 0:
                                if num == 0:
                                    soltem1 = tempp
                                else:
                                    soltem1 = soltem1 + '\n' + tempp
                            else:
                                for lli in soup.find_all('div', 'gpmsg_soln')[0].find_all('p')[num].find_all('a'):
                                    dizhi = 'http://resources.arcgis.com' + lli.get('href')
                                    dtext = lli.text
                                    newdtext = '[url=%s]%s[/url]' % (dizhi, dtext)
                                    if num == 0:
                                        soltem1 = tempp.replace(dtext, newdtext)
                                    else:
                                        soltem1 = soltem1 + '\n' + tempp.replace(dtext, newdtext)
                    print title
                    decc='[b]【问题描述】[/b]'+'\n'+decc
                    print decc
                    sol='[b]【解决方案】[/b]'+'\n'+soltem1+'\n'+'\n'+'[b]【原文链接】[/b]'+'\n'+'[b][url=%s]%s[/url][/b]'%(link,link)
                    print sol
                    # zhuanti='工具错误和警告'
                    # huati='Desktop错误和警告'
                    # sour=''
                    # hd2=''
                    # hd3=''
                    # fenlei=''
                    # fenxiangren=''
                    # cpmc='ArcGIS for Desktop'
                    # files = open(r'C:\Users\Esri\Desktop\soltion1.txt', 'a+')
                    # files.write("%s·%s·%s·%s·%s·%s·%s·%s·%s·%s·%s·%s"%(i,title,decc,zhuanti,huati,sour,sol,hd2,hd3,fenlei,fenxiangren,cpmc)+'\n')
                    worksheet.write(row, 0, i)
                    worksheet.write(row, 1, title)
                    worksheet.write(row, 2, decc)
                    worksheet.write(row, 3, sol)
                    # worksheet.write(row, 4, link)
                    row += 1
                except Exception,e:
                    errorr.append(link)
                    print link+'出错'
                    print e
                    continue
excx.close()
print errorr
print len(errorr)
        # driver = webdriver.PhantomJS(executable_path=r'D:\Python27\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        # driver.get("link")
        # data = driver.page_source
        # # print(data)
        # driver.close()
        # bfcontent = BeautifulSoup(data, 'lxml')
        # print bfcontent

    # print data['tree'][data["rootElement"]]["c"] #大类
    # print data['tree'][data['tree'][data["rootElement"]]["c"][0]]["c"] #二类
    # print data['tree'][data['tree'][data['tree'][data["rootElement"]]["c"][0]]["c"][0]]['l'] #详情
    #
    # print json.dumps(data, encoding="UTF-8", ensure_ascii=False)

# http://resources.arcgis.com/zh-cn/help/main/10.2/00vv/00vv00000002050017.htm
