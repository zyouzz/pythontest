#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import json
import geocoder
lines=open(r'C:\Users\Esri\Desktop\daxue.txt', 'r').readlines()
ee=[]
i=1
for line in lines:
    name=line.split('|')[0]
    print name
    try:
        bai = geocoder.baidu(name, key='F0968e1e1a99337902588c90500505b5')
        gbai=json.loads(json.dumps(bai.json))
        print gbai
        print gbai['lat'],gbai['lng']
        filess = open(r'C:\Users\Esri\Desktop\daxue1.txt', 'a+')
        filess.write(('%s|%s|%s'%(gbai['lat'],gbai['lng'],line)))
    except Exception,e:
        ee.append(str(i)+":"+name)
        filess = open(r'C:\Users\Esri\Desktop\daxue1.txt', 'a+')
        filess.write(line)
        continue
    i+=1
print ee


