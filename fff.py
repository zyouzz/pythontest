#-*-coding:utf-8 -*-
__author__ = 'jiang'
#使用高德API
import requests
def geocodeG(address):
    par = {'address': address, 'key': 'cb649a25c1f81c1451adbeca73623251'}
    base = 'http://restapi.amap.com/v3/geocode/geo'
    response = requests.get(base, par)
    answer = response.json()
    GPS=answer['geocodes'][0]['location'].split(",")
    return GPS[0],GPS[1]

#使用百度API
def geocodeB(address):
    base ="http://api.map.baidu.com/geocoder?address=" + address + "&output=json&key=f247cdb592eb43ebac6ccd27f796e2d2"
    response = requests.get(base)
    answer = response.json()
    return answer['result']['location']['lng'],answer['result']['location']['lat']
if __name__ == '__main__':
    print type('西那样')
    print geocodeB('[湖北,恩施]')
