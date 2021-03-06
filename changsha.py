#!/usr/bin/env python
#-*-coding:utf-8 -*-
__author__ = 'jiang'
import urllib2
import BeautifulSoup
import re
import datetime
starttime = datetime.datetime.now()
header = {'Host': 'cs.lianjia.com','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Connection': 'keep-alive'}
paath = 'C://Users//Esri//Desktop//原始数据.txt'
# log = open(paath.decode('utf-8'), 'w')
# loghead = "id" + ',' + "挂牌时间" + ',' + "经度" + ',' + "纬度" + ',' + "地点" + ',' + "小区名字" + ',' + "面积（平方米）" + ',' + "总价（万元）" + ',' + "均价（元/平方米）" + ',' + "房屋户型" + ',' + "所在楼层" + ',' + "户型结构" + ',' + "套内面积" + ',' + "建筑类型" + ',' + "房屋朝向" + ',' + "建筑结构" + ',' + "装修情况" + ',' + "梯户比例" + ',' + "配备电梯" + ',' + "产权年限" + ',' + "交易权属" + ',' + "上次交易" + ',' + "房屋用途" + ',' + "房本年限" + ',' + "产权所属" + ',' + "抵押信息" + ',' + "房本备件" +',' + "网址" + '\n'
# log.write(loghead)  # 写文件头
# log.close()
urllist=[]
id=474
for num in range(16,101):
    # print '正在爬取第%d页'%num
    if num!=0:
        url = 'http://cs.lianjia.com/ershoufang/pg'+str(num)+'co32/'
        print url
        try:
            req = urllib2.Request(str(url), headers=header)
            con = urllib2.urlopen(req)
            # 对con这个对象调用read()方法，返回的是html页面，也就是有html标签的纯文本
            doc = con.read()
            soup = BeautifulSoup.BeautifulSoup(doc)
            # print soup
            house = soup.findAll('li', {'class': 'clear'})
            #i = 0
            for houn in house:
                houseurl = re.sub(r'<li class="clear"><a class="img " href="|" target="_blank".*', '', str(houn))
                #i += 1
                urllist.append(houseurl)
                #抓取详情页
                try:
                    print '正在爬取第%d页' % num + str(id) + '条' + ' ' + '%s的详情信息' % houseurl
                    req1 = urllib2.Request(houseurl, headers=header)
                    con1 = urllib2.urlopen(req1)
                    doc1 = con1.read()
                    soup1 = BeautifulSoup.BeautifulSoup(doc1)
                    # 总价
                    price1 = soup1.findAll('span', {'class': 'total'})
                    zj = re.sub(r'<span class="total">|<.*>', '', str(price1[0]))
                    # print price
                    # 经纬度
                    loca = re.findall(r"resblockPosition.+", str(soup1))
                    # print loca[0]
                    loca1 = re.sub('resblockPosition:\'|\'.*', '', str(loca[0])).split(',')
                    jd = loca1[0]
                    wd = loca1[1]
                    # 挂牌时间
                    gpsj = re.findall(r"<span class=\"label\">挂牌时间</span>.+", str(soup1))[0].split('</span>')[1].replace('</li>', '')
                    # 地点
                    place1 = soup1.findAll('span', {'class': 'info'})
                    dd = re.sub(r'<.+?>', '', str(place1[0])).replace('&nbsp;', ' ')
                    # 小区名字
                    name1 = soup1.findAll('div', {'class': 'communityName'})
                    xqmz = re.sub(r'<.+?>', '', str(name1[0])).split('\n')[3]
                    # 面积
                    mj = re.findall(r"<span class=\"label\">建筑面积</span>.+", str(soup1))[0].split('</span>')[1].replace( '</li>', '').replace('㎡', '')
                    # 均价
                    aprice1 = soup1.findAll('span', {'class': 'unitPriceValue'})
                    jj = re.sub(r'<.+?>', '', str(aprice1[0])).replace('元/平米', '')
                    # 房屋户型
                    fwhx = re.findall(r"<span class=\"label\">房屋户型</span>.+", str(soup1))[0].split('</span>')[1].replace('</li>', '')
                    # 所在楼层
                    szlc = re.findall(r"<span class=\"label\">所在楼层</span>.+", str(soup1))[0].split('</span>')[1].replace('</li>', '')
                    # 户型结构
                    hxjg = re.findall(r"<span class=\"label\">户型结构</span>.+", str(soup1))[0].split('</span>')[1].replace('</li>', '')
                    # print hxjg
                    # 套内面积
                    tnmj = re.findall(r"<span class=\"label\">套内面积</span>.+", str(soup1))[0].split('</span>')[1].replace('</li>', '')
                    # print tnmj
                    # 建筑类型
                    jznx = re.findall(r"<span class=\"label\">建筑类型</span>.+", str(soup1))[0].split('</span>')[1].replace('</li>', '')
                    # print jznx
                    # 房屋朝向
                    fwcx = re.findall(r"<span class=\"label\">房屋朝向</span>.+", str(soup1))[0].split('</span>')[1].replace('</li>', '')
                    # print fwcx
                    # 建筑结构
                    jzjg = re.findall(r"<span class=\"label\">建筑结构</span>.+", str(soup1))[0].split('</span>')[1].replace('</li>', '')
                    # print jzjg
                    # 装修情况
                    zxqk = re.findall(r"<span class=\"label\">装修情况</span>.+", str(soup1))[0].split('</span>')[1].replace('</li>', '')
                    # print zxqk
                    # 梯户比例
                    thbl = re.findall(r"<span class=\"label\">梯户比例</span>.+", str(soup1))[0].split('</span>')[1].replace('</li>', '')
                    # print thbl
                    # 配备电梯
                    pbdt = re.findall(r"<span class=\"label\">配备电梯</span>.+", str(soup1))[0].split('</span>')[1].replace('</li>', '')
                    # print pbdt
                    # 产权年限
                    cqnx = re.findall(r"<span class=\"label\">产权年限</span>.+", str(soup1))[0].split('</span>')[1].replace('</li>', '')
                    # print cqnx
                    # 交易权属
                    jyqs = re.findall(r"<span class=\"label\">交易权属</span>.+", str(soup1))[0].split('</span>')[1].replace('</li>', '')
                    # print jyqs
                    # 上次交易
                    scjy = re.findall(r"<span class=\"label\">上次交易</span>.+", str(soup1))[0].split('</span>')[1].replace('</li>', '')
                    # print scjy
                    # 房屋用途
                    fwyt = re.findall(r"<span class=\"label\">房屋用途</span>.+", str(soup1))[0].split('</span>')[1].replace('</li>', '')
                    # print fwyt
                    # 房本年限
                    fbnx = re.findall(r"<span class=\"label\">房本年限</span>.+", str(soup1))[0].split('</span>')[1].replace('</li>', '')
                    # print fbnx
                    # 产权所属
                    cqss = re.findall(r"<span class=\"label\">产权所属</span>.+", str(soup1))[0].split('</span>')[1].replace('</li>', '')
                    # print cqss
                    # 抵押信息
                    dyxx1 = re.findall(r"<span class=\"label\">抵押信息</span>.+", str(soup1))[0].split('</span>')[1].replace('</li>', '')
                    dyxx = re.sub(r'<.*>', '', dyxx1)
                    # print dyxx
                    # 房本备件
                    fbbj = re.findall(r"<span class=\"label\">房本备件</span>.+", str(soup1))[0].split('</span>')[1].replace('</li>', '')
                    # print fbbj
                    id+=1
                    file = open(paath.decode('utf-8'), 'a')
                    line = str(id) + ',' + gpsj + ',' + jd + ',' + wd + ',' + dd + ',' + xqmz + ',' + mj + ',' + zj + ',' + jj + ',' + fwhx + ',' + szlc + ',' + hxjg + ',' + tnmj + ',' + jznx + ',' + fwcx + ',' + jzjg + ',' + zxqk + ',' + thbl + ',' + pbdt + ',' + cqnx + ',' + jyqs + ',' + scjy + ',' + fwyt + ',' + fbnx + ',' + cqss + ',' + dyxx + ',' + fbbj +',' + houseurl + '\n'
                    file.write(line)
                    file.close()
                except Exception, e:
                    print  e

        except Exception, e:
            print  e
    else:
        url='http://cs.lianjia.com/ershoufang/co32/'
        try:
            req = urllib2.Request(url, headers=header)
            con = urllib2.urlopen(req)
            # 对con这个对象调用read()方法，返回的是html页面，也就是有html标签的纯文本
            doc = con.read()
            soup = BeautifulSoup.BeautifulSoup(doc)
            # print soup
            house = soup.findAll('li', {'class': 'clear'})
            #i = 0
            for houn in house:
                houseurl = re.sub(r'<li class="clear"><a class="img " href="|" target="_blank".*', '', str(houn))
                #i += 1
                urllist.append(houseurl)
                # 抓取详情页
                try:
                    print '正在爬取第%d页' % num + str(id) + '条' + ' ' + '%s的详情信息' % houseurl
                    req1 = urllib2.Request(houseurl, headers=header)
                    con1 = urllib2.urlopen(req1)
                    doc1 = con1.read()
                    soup1 = BeautifulSoup.BeautifulSoup(doc1)
                    # 总价
                    price1 = soup1.findAll('span', {'class': 'total'})
                    zj = re.sub(r'<span class="total">|<.*>', '', str(price1[0]))
                    # print price
                    # 经纬度
                    loca = re.findall(r"resblockPosition.+", str(soup1))
                    # print loca[0]
                    loca1 = re.sub('resblockPosition:\'|\'.*', '', str(loca[0])).split(',')
                    jd = loca1[0]
                    wd = loca1[1]
                    # 挂牌时间
                    gpsj = re.findall(r"<span class=\"label\">挂牌时间</span>.+", str(soup1))[0].split('</span>')[
                        1].replace('</li>', '')
                    # 地点
                    place1 = soup1.findAll('span', {'class': 'info'})
                    dd = re.sub(r'<.+?>', '', str(place1[0])).replace('&nbsp;', ' ')
                    # 小区名字
                    name1 = soup1.findAll('div', {'class': 'communityName'})
                    xqmz = re.sub(r'<.+?>', '', str(name1[0])).split('\n')[3]
                    # 面积
                    mj = re.findall(r"<span class=\"label\">建筑面积</span>.+", str(soup1))[0].split('</span>')[1].replace('</li>', '').replace('㎡', '')
                    # 均价
                    aprice1 = soup1.findAll('span', {'class': 'unitPriceValue'})
                    jj = re.sub(r'<.+?>', '', str(aprice1[0])).replace('元/平米', '')
                    # 房屋户型
                    fwhx = re.findall(r"<span class=\"label\">房屋户型</span>.+", str(soup1))[0].split('</span>')[
                        1].replace('</li>', '')
                    # 所在楼层
                    szlc = re.findall(r"<span class=\"label\">所在楼层</span>.+", str(soup1))[0].split('</span>')[
                        1].replace('</li>', '')
                    # 户型结构
                    hxjg = re.findall(r"<span class=\"label\">户型结构</span>.+", str(soup1))[0].split('</span>')[
                        1].replace('</li>', '')
                    # print hxjg
                    # 套内面积
                    tnmj = re.findall(r"<span class=\"label\">套内面积</span>.+", str(soup1))[0].split('</span>')[
                        1].replace('</li>', '')
                    # print tnmj
                    # 建筑类型
                    jznx = re.findall(r"<span class=\"label\">建筑类型</span>.+", str(soup1))[0].split('</span>')[
                        1].replace('</li>', '')
                    # print jznx
                    # 房屋朝向
                    fwcx = re.findall(r"<span class=\"label\">房屋朝向</span>.+", str(soup1))[0].split('</span>')[
                        1].replace('</li>', '')
                    # print fwcx
                    # 建筑结构
                    jzjg = re.findall(r"<span class=\"label\">建筑结构</span>.+", str(soup1))[0].split('</span>')[
                        1].replace('</li>', '')
                    # print jzjg
                    # 装修情况
                    zxqk = re.findall(r"<span class=\"label\">装修情况</span>.+", str(soup1))[0].split('</span>')[
                        1].replace('</li>', '')
                    # print zxqk
                    # 梯户比例
                    thbl = re.findall(r"<span class=\"label\">梯户比例</span>.+", str(soup1))[0].split('</span>')[
                        1].replace('</li>', '')
                    # print thbl
                    # 配备电梯
                    pbdt = re.findall(r"<span class=\"label\">配备电梯</span>.+", str(soup1))[0].split('</span>')[
                        1].replace('</li>', '')
                    # print pbdt
                    # 产权年限
                    cqnx = re.findall(r"<span class=\"label\">产权年限</span>.+", str(soup1))[0].split('</span>')[
                        1].replace('</li>', '')
                    # print cqnx
                    # 交易权属
                    jyqs = re.findall(r"<span class=\"label\">交易权属</span>.+", str(soup1))[0].split('</span>')[
                        1].replace('</li>', '')
                    # print jyqs
                    # 上次交易
                    scjy = re.findall(r"<span class=\"label\">上次交易</span>.+", str(soup1))[0].split('</span>')[
                        1].replace('</li>', '')
                    # print scjy
                    # 房屋用途
                    fwyt = re.findall(r"<span class=\"label\">房屋用途</span>.+", str(soup1))[0].split('</span>')[
                        1].replace('</li>', '')
                    # print fwyt
                    # 房本年限
                    fbnx = re.findall(r"<span class=\"label\">房本年限</span>.+", str(soup1))[0].split('</span>')[
                        1].replace('</li>', '')
                    # print fbnx
                    # 产权所属
                    cqss = re.findall(r"<span class=\"label\">产权所属</span>.+", str(soup1))[0].split('</span>')[
                        1].replace('</li>', '')
                    # print cqss
                    # 抵押信息
                    dyxx1 = re.findall(r"<span class=\"label\">抵押信息</span>.+", str(soup1))[0].split('</span>')[
                        1].replace('</li>', '')
                    dyxx = re.sub(r'<.*>', '', dyxx1)
                    # print dyxx
                    # 房本备件
                    fbbj = re.findall(r"<span class=\"label\">房本备件</span>.+", str(soup1))[0].split('</span>')[
                        1].replace('</li>', '')
                    # print fbbj
                    file = open(paath.decode('utf-8'), 'a')
                    id+=1
                    line = str(id) + ',' + gpsj + ',' + jd + ',' + wd + ',' + dd + ',' + xqmz + ',' + mj + ',' + zj + ',' + jj + ',' + fwhx + ',' + szlc + ',' + hxjg + ',' + tnmj + ',' + jznx + ',' + fwcx + ',' + jzjg + ',' + zxqk + ',' + thbl + ',' + pbdt + ',' + cqnx + ',' + jyqs + ',' + scjy + ',' + fwyt + ',' + fbnx + ',' + cqss + ',' + dyxx + ',' + fbbj + ',' + houseurl + '\n'
                    file.write(line)
                    file.close()
                except Exception, e:
                    print  e

        except Exception, e:
            print  e

endtime = datetime.datetime.now()
time = (endtime - starttime).seconds
print "最终共爬取到"+str(id)+"条信息"
print "用时"+str(time)+"秒"


