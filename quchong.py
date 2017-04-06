#!/usr/bin/env python
#-*-coding:utf-8 -*-
__author__ = 'jiang'
import re
lines_seen = set()
outfile = open("C://Users//Esri//Desktop//duplicate.txt","w")
for line in open("C://Users//Esri//Desktop//log.txt","r"):
    rline1=line.split(',')[0]
    print(rline1)
    rline2=line.split(',')[2]
    print(rline2)
    rline3=line.split(',')[1][:-9]
    print(rline3)
    reline=rline1+','+rline3+','+rline2
    if reline not in lines_seen:
        print(reline)
        outfile.write(reline)
        lines_seen.add(reline)
f = open("C://Users//Esri//Desktop//duplicate.txt", "r+")
open('C://Users//Esri//Desktop//duplicate1.txt', 'w').write(re.sub(r'IP,,搜索关键词', 'IP,日期,搜索关键词', f.read()))
# for seen in lines_seen:
#     print(seen)
