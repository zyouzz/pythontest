# !/usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib
import urllib2
import requests
import datetime

class Location_Sina():
    """
    Interface of sina
    Under my test is of higher recognition and performance at home
    """

    def __init__(self, ip):
        self.ip = urllib.quote_plus(ip)
        self.api_url = 'http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js&ip=%s' % self.ip

    def get_geoinfo(self):
        urlobj = urllib2.urlopen(self.api_url)
        data = urlobj.read()[20:][:-1]
        datadict = json.loads(data, encoding='utf-8')
        return datadict

    def get_country(self):
        datadict = self.get_geoinfo()
        return datadict['country']

    def get_province(self):
        datadict = self.get_geoinfo()
        return datadict['province']

    def get_city(self):
        datadict = self.get_geoinfo()
        return datadict['city']


class Location_Taobao():
    """
    Interface of taobao
    Under my test can be the 2ed choice
    """

    def __init__(self, ip):
        self.ip = urllib.quote_plus(ip)
        self.api_url = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s' % self.ip

    def get_geoinfo(self):
        urlobj = urllib2.urlopen(self.api_url)
        data = urlobj.read()
        datadict = json.loads(data, encoding='utf-8')
        return datadict['data']

    def get_country(self):
        datadict = self.get_geoinfo()
        return datadict['country']

    def get_province(self):
        datadict = self.get_geoinfo()
        return datadict['region']

    def get_city(self):
        datadict = self.get_geoinfo()
        return datadict['city']

    def get_isp(self):
        datadict = self.get_geoinfo()
        return datadict['isp']


class Location_Freegeoip():
    """
    Interface of an excellent foreign service freegeoip
    The only shortage may be it return result in English
    """

    def __init__(self, ip):
        self.ip = urllib.quote_plus(ip)
        self.api_url = 'http://freegeoip.net/json/%s' % (self.ip)

    def get_geoinfo(self):
        urlobj = urllib2.urlopen(self.api_url)
        data = urlobj.read()
        datadict = json.loads(data, encoding='utf-8')
        return datadict

    def get_country(self):
        datadict = self.get_geoinfo()
        return datadict['country_name']

    def get_province(self):
        datadict = self.get_geoinfo()
        return datadict['region_name']

    def get_city(self):
        datadict = self.get_geoinfo()
        return datadict['city']


def ip2loc(ip):
    """
    An integrated user defined function via three APIs to transform IP to specific geographic position
    :param ip:IP
    :return:a list of ["country(or other)", "province(or other)", "city(or other)"]
    """
    try:
        loc = [Location_Sina(ip).get_country(), Location_Sina(ip).get_province(), Location_Sina(ip).get_city()]
        if all(loc):
            pass
        else:
            for i in range(len(loc)):
                if loc[i]:
                    pass
                else:
                    if i == 0:
                        loc[i] = Location_Taobao(ip).get_country()
                    elif i == 1:
                        loc[i] = Location_Taobao(ip).get_province()
                    elif i == 2:
                        loc[i] = Location_Taobao(ip).get_city()
            if all(loc):
                pass
            else:
                for j in range(len(loc)):
                    if loc[j]:
                        pass
                    else:
                        if j == 0:
                            loc[j] = Location_Freegeoip(ip).get_country()
                        elif j == 1:
                            loc[j] = Location_Freegeoip(ip).get_province()
                        elif j == 2:
                            loc[j] = Location_Freegeoip(ip).get_city()
                if all(loc):
                    pass
                else:
                    for k in range(len(loc)):
                        if loc[k]:
                            pass
                        else:
                            loc[k] = "暂未识别"
        return loc
    except:
        loc = ["无法处理", "无法处理", "无法处理"]
        return loc
def geocodeB(address):
    base =url="http://api.map.baidu.com/geocoder?address=" + address + "&output=json&key=f247cdb592eb43ebac6ccd27f796e2d2"
    # if  requests.get(base,timeout=3):
    response = requests.get(base, timeout=3)
    # print 'rep'
    answer = response.json()
    # print 'ans'
    return answer['result']['location']['lng'],answer['result']['location']['lat']

if __name__ == '__main__':
    # ip = '124.205.245.98'
    soucrdata = open(r'C:\Users\Esri\Desktop\statistics\nodate.txt', "r").read().split('\n')
    sf=open(r'C:\Users\Esri\Desktop\ip地址.txt'.decode('utf-8'), "w")
    loghead = "IP" + ',' + "国家"+ ',' + "省"+ ',' + "市"+ ',' + "经度"+ ',' + "纬度"+ ',' + "年"+ ',' + "月"+ ',' + "日"+ ',' + "关键词" '\n'
    sf.write(loghead)  # 写文件头
    sf.close()
    i=0
    for ips in soucrdata[1:len(soucrdata) - 1]:
        ip = ips.split(',')[0]
        # print ip
        date = ips.split(',')[1].split('/')
        year = date[2]
        month = date[1]
        day = date[0]
        keyword = ips.split(',')[2]
        loc = ip2loc(ip)
        guojia=loc[0]
        sheng=loc[1]
        shi=loc[2]
        # print type(shi.encode('utf-8'))
        # print geocodeB('常德')
        i += 1
        try:
            # time1=datetime.datetime.now()
            jw=geocodeB(guojia+' '+sheng+' '+shi)
            jingdu=jw[0]
            weidu=jw[1]

            # print(loc)
            # print(loc[0],loc[1],loc[2])
            # print(loc[1])
            # print(loc[2])

            print str(i)+','+ip+','+guojia.encode('utf-8')+','+sheng.encode('utf-8')+','+shi.encode('utf-8')+','+str(jingdu)+','+str(weidu)
            sf = open(r'C:\Users\Esri\Desktop\ip地址.txt'.decode('utf-8'), "a")
            sf.write(ip+','+guojia.encode('utf-8')+','+sheng.encode('utf-8')+','+shi.encode('utf-8')+','+str(jingdu)+','+str(weidu)+','+year+','+month+','+day+','+keyword+'\n')
            pass
        except Exception,e:
            print e
            continue
