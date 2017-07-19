#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import os
import xlsxwriter
import sys
reload(sys)
sys.setdefaultencoding('utf8')
content= open(r'C:\Users\Esri\Desktop\soltion1.txt','r').read()
folder1='C:\Users\Esri\Desktop'
xlsx11=os.path.join(folder1, "solution615.xlsx")
print xlsx11
excx = xlsxwriter.Workbook(xlsx11)
worksheet = excx.add_worksheet()
for i in range(2622):
    if i==0:
        ss=content.split(str((i + 1)) + '·')[0].replace(str(i)+'·','')
    elif i==2621:
        ss=content.split(str(i) + '·')[1]
    else:
        ss=content.split(str(i) + '·')[1].split(str((i + 1)) + '·')[0]
    sf=ss.split('·')
    bianhao=i
    jd=sf[0]
    xxms=sf[1]
    zt=sf[2]
    ht=sf[3]
    wtly=sf[4]
    hd1=sf[5]
    hd2=sf[6]
    hd3=sf[7]
    flid=sf[8]
    fxr=sf[9]
    cpmc=sf[10]
    worksheet.write(i, 0, bianhao)
    worksheet.write(i, 1, jd)
    worksheet.write(i, 2, xxms)
    worksheet.write(i, 3, zt)
    worksheet.write(i, 4, ht)
    worksheet.write(i, 5, wtly)
    worksheet.write(i, 6, hd1)
    worksheet.write(i, 7, hd2)
    worksheet.write(i, 8, hd3)
    worksheet.write(i, 9, flid)
    worksheet.write(i, 10, fxr)
    worksheet.write(i, 11, cpmc)
excx.close()

