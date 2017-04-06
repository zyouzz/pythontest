#!/usr/bin/env python
# -*-coding:utf-8 -*-
#__author__ = 'jiang'
dayst=open(r'C://Users//Esri//Desktop//statistics//每天搜索次数统计.txt',encoding='utf-8').readlines()
print(dayst)
da=[]
fre=[]
for tx1 in dayst:
    da.append(tx1.split(',')[0])
    fre.append(tx1.split(',')[1].replace('\n',''))
file=open(r'C:\Users\Esri\Desktop\statistics\每天统计.html',encoding='utf-8').readlines()
file[22]=str(da)+','+'\n'
file[24]=str(fre)+','+'\n'
file1=open(r'C:\Users\Esri\Desktop\statistics\每天统计.html','w+',encoding='utf-8')
file1.writelines(file)
file1.close()

