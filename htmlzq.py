#!/usr/bin/env python
# -*-coding:utf-8 -*-
import urllib2
import urllib
import BeautifulSoup
import re
import datetime
__author__ = 'jiang'
header = {'Host': 'cs.lianjia.com','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Connection': 'keep-alive'}
paath1 = 'C://Users//Esri//Desktop//网址.txt'
log = open(paath1.decode('utf-8'), 'r').read()
paath = 'C://Users//Esri//Desktop//原始数据.txt'
id=474
for wz in log.split('\n'):
    print wz

    try:
        print '正在爬取第' + str(id) + '条' + ' ' + '%s的详情信息' % wz
        req = urllib.urlopen(wz, proxies={"http": "http://154.127.52.247:8080"})
        doc = req.read()
        soup1 = BeautifulSoup.BeautifulSoup(doc)
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
        gpsj = re.findall(r"<span class=\"label\">挂牌时间</span>.+", str(soup1))[0].split('</span>')[1].replace(
            '</li>', '')
        # 地点
        place1 = soup1.findAll('span', {'class': 'info'})
        dd = re.sub(r'<.+?>', '', str(place1[0])).replace('&nbsp;', ' ')
        # 小区名字
        name1 = soup1.findAll('div', {'class': 'communityName'})
        xqmz = re.sub(r'<.+?>', '', str(name1[0])).split('\n')[3]
        # 面积
        mj = re.findall(r"<span class=\"label\">建筑面积</span>.+", str(soup1))[0].split('</span>')[1].replace(
            '</li>', '').replace('㎡', '')
        # 均价
        aprice1 = soup1.findAll('span', {'class': 'unitPriceValue'})
        jj = re.sub(r'<.+?>', '', str(aprice1[0])).replace('元/平米', '')
        # 房屋户型
        fwhx = re.findall(r"<span class=\"label\">房屋户型</span>.+", str(soup1))[0].split('</span>')[1].replace(
            '</li>', '')
        # 所在楼层
        szlc = re.findall(r"<span class=\"label\">所在楼层</span>.+", str(soup1))[0].split('</span>')[1].replace(
            '</li>', '')
        # 户型结构
        hxjg = re.findall(r"<span class=\"label\">户型结构</span>.+", str(soup1))[0].split('</span>')[1].replace(
            '</li>', '')
        # print hxjg
        # 套内面积
        tnmj = re.findall(r"<span class=\"label\">套内面积</span>.+", str(soup1))[0].split('</span>')[1].replace(
            '</li>', '')
        # print tnmj
        # 建筑类型
        jznx = re.findall(r"<span class=\"label\">建筑类型</span>.+", str(soup1))[0].split('</span>')[1].replace(
            '</li>', '')
        # print jznx
        # 房屋朝向
        fwcx = re.findall(r"<span class=\"label\">房屋朝向</span>.+", str(soup1))[0].split('</span>')[1].replace(
            '</li>', '')
        # print fwcx
        # 建筑结构
        jzjg = re.findall(r"<span class=\"label\">建筑结构</span>.+", str(soup1))[0].split('</span>')[1].replace(
            '</li>', '')
        # print jzjg
        # 装修情况
        zxqk = re.findall(r"<span class=\"label\">装修情况</span>.+", str(soup1))[0].split('</span>')[1].replace(
            '</li>', '')
        # print zxqk
        # 梯户比例
        thbl = re.findall(r"<span class=\"label\">梯户比例</span>.+", str(soup1))[0].split('</span>')[1].replace(
            '</li>', '')
        # print thbl
        # 配备电梯
        pbdt = re.findall(r"<span class=\"label\">配备电梯</span>.+", str(soup1))[0].split('</span>')[1].replace(
            '</li>', '')
        # print pbdt
        # 产权年限
        cqnx = re.findall(r"<span class=\"label\">产权年限</span>.+", str(soup1))[0].split('</span>')[1].replace(
            '</li>', '')
        # print cqnx
        # 交易权属
        jyqs = re.findall(r"<span class=\"label\">交易权属</span>.+", str(soup1))[0].split('</span>')[1].replace(
            '</li>', '')
        # print jyqs
        # 上次交易
        scjy = re.findall(r"<span class=\"label\">上次交易</span>.+", str(soup1))[0].split('</span>')[1].replace(
            '</li>', '')
        # print scjy
        # 房屋用途
        fwyt = re.findall(r"<span class=\"label\">房屋用途</span>.+", str(soup1))[0].split('</span>')[1].replace(
            '</li>', '')
        # print fwyt
        # 房本年限
        fbnx = re.findall(r"<span class=\"label\">房本年限</span>.+", str(soup1))[0].split('</span>')[1].replace(
            '</li>', '')
        # print fbnx
        # 产权所属
        cqss = re.findall(r"<span class=\"label\">产权所属</span>.+", str(soup1))[0].split('</span>')[1].replace(
            '</li>', '')
        # print cqss
        # 抵押信息
        dyxx1 = re.findall(r"<span class=\"label\">抵押信息</span>.+", str(soup1))[0].split('</span>')[1].replace(
            '</li>', '')
        dyxx = re.sub(r'<.*>', '', dyxx1)
        # print dyxx
        # 房本备件
        fbbj = re.findall(r"<span class=\"label\">房本备件</span>.+", str(soup1))[0].split('</span>')[1].replace(
            '</li>', '')
        # print fbbj
        id += 1
        file = open(paath.decode('utf-8'), 'a')
        line = str(id) + ',' + gpsj + ',' + jd + ',' + wd + ',' + dd + ',' + xqmz + ',' + mj + ',' + zj + ',' + jj + ',' + fwhx + ',' + szlc + ',' + hxjg + ',' + tnmj + ',' + jznx + ',' + fwcx + ',' + jzjg + ',' + zxqk + ',' + thbl + ',' + pbdt + ',' + cqnx + ',' + jyqs + ',' + scjy + ',' + fwyt + ',' + fbnx + ',' + cqss + ',' + dyxx + ',' + fbbj + ',' + wz + '\n'
        file.write(line)
        file.close()
    except Exception, e:
        print  e
