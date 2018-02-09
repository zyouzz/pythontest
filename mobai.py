#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
#!/usr/bin/env python
# coding: utf8

import time

import requests

session = requests.Session()
session.headers['host'] = 'mwx.mobike.com'
session.headers['content-type'] = 'application/x-www-form-urlencoded'
session.headers['opensrc'] = 'list'
session.headers['mobileno'] = ''
session.headers['wxcode'] = 'fake wxcode'
session.headers['platform'] = '3'
session.headers['accept-language'] = 'zh-cn'
session.headers['subsource'] = ''
session.headers['lang'] = 'zh'
session.headers['user-agent'] = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (' \
                                'KHTML, like Gecko) Mobile/15A432 MicroMessenger/6.5.19 NetType/WIFI Language/zh_CN'
session.headers['referer'] = 'https://servicewechat.com/fake/137/page-frame.html'


def main():
    session.headers['time'] = str(long(time.time() * 1000))
    session.headers['citycode'] = '010'

    body = {
        'verticalAccuracy': 10,
        'speed': -1,
        'horizontalAccuracy': 65,
        'accuracy': 65,
        'errMsg': 'getLocation:ok',
        'citycode': '010',
        'wxcode': 'fake wxcode',
        'longitude': '116.302951',
        'latitude': '39.961638',
        'altitude': '46.802894592285156',
    }
    for i in range(1,5):
        body['longitude']=str((2*i-1)*5000/20037508.34*180+116.302951)
        for j in range(1,5):
            body['altitude'] = str(39.961638-(2 * j - 1) * 5000 / 20037508.34 * 180)
            print body['longitude']
            data = session.post(url='https://mwx.mobike.com/mobike-api/rent/nearbyBikesInfo.do', data=body).json()

            for bike in data['object']:
                # print '{distId}\t{distX}\t{distY}\t{distance}\t{biketype}'.format(**bike)
                print bike['distId']
                filers = open(r'C:\Users\Esri\Desktop\url55.txt', 'a+')
                filers.write(str(bike['distId'])+";"+str(bike['distX'])+";"+str(bike['distY'])+"\n")


if __name__ == '__main__':
    main()