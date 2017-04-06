#!/usr/bin/env python
#-*-coding:utf-8 -*-
__author__ = 'jiang'
import os
import re
import collections
outfile = open("C://Users//Esri//Desktop//frequency.txt","w")
for line in open("C://Users//Esri//Desktop//duplicate1.txt","r"):
    reline1=line.split(',')[2]
    outfile.write(reline1)
outfile.close()
f1= open("C://Users//Esri//Desktop//frequency.txt", "r+")
f2= open('C://Users//Esri//Desktop//frequency1.txt', 'w')
f2.write(re.sub(r'搜索关键词', '', f1.read()))
f1.close()
f2.close()
str1=open('C://Users//Esri//Desktop//frequency1.txt').read().split()
print(str1)
print("原文本:\n %s"% str1)
print("\n各词出现的次数：\n %s" % collections.Counter(str1))
print(collections.Counter(str1)['arcgis'])#以字典的形式存储，每个字符对应的键值就是在文本中出现的次数