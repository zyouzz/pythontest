# #!/usr/bin/env python
# # -*-coding:utf-8 -*-
# __author__ = 'jiang'
from bs4 import BeautifulSoup
from selenium import webdriver


def get_zhuanye(url):
    print(url)
    driver = webdriver.PhantomJS(executable_path=r'D:\Python27\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    driver.get(url)
    data = driver.page_source
    # print(data)
    driver.close()
    bfcontent = BeautifulSoup(data, 'lxml')
    zhuanye = bfcontent.find_all('tbody', 'lin-seachtable')[0].find_all('tr')
    # print zhuanye
    for zy in zhuanye:
        # print zy
        zyin=zy.find_all('td')
        #学校名称
        name=zyin[0].find_all('a')[0].get('title')
        #专业名称
        zhuanyename = zyin[1].text
        #是否重点专业
        vip = zyin[2].text
        #院校属性
        if zyin[3].get('style'):
            shuxing = '非教育部直属'.decode('utf8')
        else:
            shuxing = zyin[3].text
        #985大学
        if zyin[4].get('style'):
            a985='非985大学'.decode('utf8')
        else:
            a985 = zyin[4].text
        #211大学
        if zyin[5].get('style'):
            a211='非211大学'.decode('utf8')
        else:
            a211 = zyin[5].text
        unilink= str(zyin[1].find_all('a')[0].get('href'))
        print name,shuxing,a985,a211
        files = open(r'C:\Users\Esri\Desktop\rs1.txt', 'a+')
        files.write(('%s,%s,%s,%s,%s,%s,%s' % (name, zhuanyename, vip, shuxing, a985, a211, unilink)) .encode('utf8')+ '\n')

for i in range(1,2):
    try:
        link='http://gkcx.eol.cn/soudaxue/querySchoolSpecialty.html?&argspecialtyname=\u9065\u611f&argzycengci=\u4e13\u79d1&page='+str(i)
        get_zhuanye(link)
    except Exception, e:
        print e