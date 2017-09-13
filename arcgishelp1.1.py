#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import os
from bs4 import BeautifulSoup
import requests
import json
import xlsxwriter
import sys
reload(sys)
sys.setdefaultencoding('utf8')

session = requests.session()
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
headers = {'User-Agent': user_agent}

folder='C:\Users\Esri\Desktop\json'
folder1='C:\Users\Esri\Desktop'
xlsx11=os.path.join(folder1, "solution101.xlsx")
print xlsx11
excx = xlsxwriter.Workbook(xlsx11)
worksheet = excx.add_worksheet()

filename=os.listdir(folder)
i = -1
row = 0
errorr=[]
folder2='C:/Users/Esri/Desktop/json/'
for name in range(2,3):
    jsonpath=folder2+str(name)+'.json'
    print jsonpath
    with open(jsonpath) as json_file:
        data = json.load(json_file)
        firsl=data['tree'][data["rootElement"]]["c"]
        print firsl
        for first in firsl[1:2]:
            second2=data['tree'][first]["c"]
            print second2
            for se in second2[3:4]:
                   for third5 in data['tree'][se]["c"][3:4]:
                      for third6 in data['tree'][third5]["c"][-1:]:
                          for third7 in data['tree'][third6]["c"]:
                           for third3 in data['tree'][third7]["c"]:
                            link='http://resources.arcgis.com/zh-cn/help/main/10.2/'+third3[:4]+'/'+third3+'.htm'
                            print link
                            print i
                            i+=1
                            page = session.get(link,headers=headers)
                            page.encoding = page.apparent_encoding
                            soup = BeautifulSoup(page.text, 'lxml')
                            try:
                                title='【Desktop】工具错误码-'+soup.title.text[19:].replace('\r\n',' ') #题目
                                print title
                                content = soup.find_all('div')[0].text.split('Copyright ©')[0].replace(soup.title.text[19:], '')

                                print content
                                if soup.find_all('a'):
                                    lls = soup.find_all('a')
                                    quchong = set(lls)
                                    # print quchong
                                    for ll in quchong:
                                        dizhi = 'http://resources.arcgis.com' + ll.get('href')
                                        dtext = ll.text
                                        newdtext = '[url=%s]%s[/url]' % (dizhi, dtext)
                                        content = content.replace(dtext, newdtext)
                                        # print content
                                s1 = content.split('解决方案')[0]
                                if '更多信息'in content.split('解决方案')[1]:

                                    print '有更多信息'
                                    if len(content.split('解决方案')) >= 3:
                                        s2 = '解决方案'.join(content.split('解决方案')[1:])
                                    else:
                                        s2 = content.split('解决方案')[1].split('更多信息')[0]
                                    s3 = content.split('更多信息')[1]
                                    s2 = s2.replace(s3, '').replace('更多信息', '')
                                    print s3
                                    decc = '[b]【问题描述】[/b]' + '\n' + s1.replace('\n', '')
                                    print decc
                                    sol = '[b]【解决方案】[/b]' + '\n' + s2.replace('\n',
                                                                              '') + '\n' + '[b]【更多信息】[/b]' + '\n' + s3 + '\n' + '[b]【原文链接】[/b]' + '\n' + '[b][url=%s]%s[/url][/b]' % (
                                        link, link)
                                    print sol
                                else:
                                    print '无更多信息'
                                    if len(content.split('解决方案')) >= 3:
                                        s2 = '解决方案'.join(content.split('解决方案')[1:])
                                    else:
                                        s2 = content.split('解决方案')[1].split('更多信息')[0]
                                    print title
                                    decc = '[b]【问题描述】[/b]' + '\n' + s1.replace('\n', '')
                                    print decc
                                    sol = '[b]【解决方案】[/b]' + '\n' + s2.replace('\n',
                                                                              '') + '\n' + '[b]【原文链接】[/b]' + '\n' + '[b][url=%s]%s[/url][/b]' % (
                                        link, link)
                                    print sol
                                worksheet.write(row, 0, i)
                                worksheet.write(row, 1, title)
                                worksheet.write(row, 2, decc)
                                worksheet.write(row, 3, sol)
                                row += 1
                            except Exception,e:
                                errorr.append(link)
                                print link+'出错'
                                print e
                                continue
excx.close()
print errorr
print len(errorr)