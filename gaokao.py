# #!/usr/bin/env python
# # -*-coding:utf-8 -*-
# __author__ = 'jiang'
from bs4 import BeautifulSoup
from selenium import webdriver


def get_university(url):
    print(url)
    driver = webdriver.PhantomJS(executable_path=r'D:\Python27\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    driver.get(url)
    data = driver.page_source
    # print(data)
    driver.close()
    bfcontent = BeautifulSoup(data, 'lxml')

    biao1=bfcontent.find_all('tr','lin-gettr')
    for uni1 in biao1:
        uni11=uni1.find_all('td')
        # print str(uni1).decode('utf8')
        # print uni1.find_all('td')
        #高校名称
        name1=uni11[0].text
        print name1
        #所在省份
        shengfen1=uni11[1].text
        print shengfen1
        #学历层次
        cengci1=uni11[2].text
        print cengci1
        #全国热度排名
        hot1=uni11[3].text
        print hot1
        #所属类别
        leibie1=uni11[4].text.split(' ')[0]
        print leibie1
        #所属类别排名
        leibiepm1=uni11[4].text.split(' ')[1]
        print leibiepm1
        #高校链接
        link1= 'http://gkcx.eol.cn'+str(uni11[0].find_all('a')[0].get('href')).strip()
        print link1
        files = open(r'C:\Users\Esri\Desktop\university.txt', 'a+')
        files.write(('%s,%s,%s,%s,%s,%s,%s'%(name1,shengfen1,cengci1,hot1,leibie1,leibiepm1,link1)).encode('utf-8')+ '\n')

    if bfcontent.find_all('tr','getJsXmlTr '):
        biao2 = bfcontent.find_all('tr', 'getJsXmlTr ')
        for uni2 in biao2:
            uni22=uni2.find_all('td')
            # print str(uni2).decode('utf8')
            # print uni2.find_all('td')
            # 高校名称
            name2 = uni22[0].find_all('a')[0].text
            print name2
            # 所在省份
            shengfen2 = uni22[1].text
            print shengfen2
            # 学历层次
            cengci2 = uni22[2].text
            print cengci2
            # 全国热度排名
            hot2 = uni22[3].text
            print hot2
            # 所属类别
            leibie2 = uni22[4].text.split(' ')[0]
            print leibie2
            # 所属类别排名
            leibiepm2 = uni22[4].text.split(' ')[1]
            print leibiepm2
            # 高校链接
            link2 = 'http://gkcx.eol.cn' + str(uni22[0].find_all('a')[0].get('href')).strip()
            print link2
            files = open(r'C:\Users\Esri\Desktop\university.txt', 'a+')
            files.write(('%s,%s,%s,%s,%s,%s,%s'%(name2,shengfen2,cengci2,hot2,leibie2,leibiepm2,link2)).encode('utf-8')+ '\n')

    # return name1,name2,shengfen1,shengfen2,cengci1,cengci2,hot1,hot2,leibie1,leibie2,leibiepm1,leibiepm2

for i in range(93,94):
    try:
        link='http://gkcx.eol.cn/soudaxue/queryschool.html?&page='+str(i)
        get_university(link)
    except Exception, e:
        print e
        continue
        # bai = geocoder.baidu('上海对外经贸大学', key='F0968e1e1a99337902588c90500505b5')
        # qbai=json.loads(json.dumps(bai.json))
        # print qbai['lat'],qbai['lng']
