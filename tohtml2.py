#!/usr/bin/env python
# -*-coding:utf-8 -*-
#__author__ = 'jiang'
dayst=open(r'C://Users//Esri//Desktop//statistics//关键词top100.txt',encoding='utf-8').readlines()
print(dayst)
da=[]
fre=[]
for tx1 in dayst:
    da.append(tx1.split(',')[0])
    fre.append(tx1.split(',')[1].replace('\n',''))
file=open(r'C:\Hexo\source\html\ArcGIS知乎站内搜索关键词统计.html',encoding='utf-8').readlines()
file[31]=str(da[:51])+','+'\n'
file[33]=str(fre[:51])+','+'\n'
file1=open(r'C:\Hexo\source\html\ArcGIS知乎站内搜索关键词统计.html','w+',encoding='utf-8')
file1.writelines(file)
file1.close()