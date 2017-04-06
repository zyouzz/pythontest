#!/usr/bin/env python
# -*-coding:utf-8 -*-
#__author__ = 'jiang'
import datetime

starttime = datetime.datetime.now()
with open(r'C:\Users\Esri\Desktop\dem.txt', 'r') as f:
    lines = f.readlines()
    i=1
    # print lines[100].replace('-9999','0')
    for line in lines:
        print '正在读取第%d行'%i
        reline=line.replace('-9999', '0')
        new = open(r'C:\Users\Esri\Desktop\newwww.txt', 'a')
        new.write(reline)
        i+=1
endtime = datetime.datetime.now()
time = (endtime - starttime).seconds
print "用时"+str(time)+"秒"
