#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
aa=[]
with open(r"C:\Users\Esri\Desktop\new 4.txt") as files:
    names=files.readlines()
    for name in names:
        print name.split('/')[-1].replace("\n",'')
        aa.append(name.split('/')[-1].replace("\n",''))
print aa
print len(aa)