#!/usr/bin/env python
#-*-coding:utf-8 -*-
#__author__ = 'jiang'

'''按月份统计汇总'''
outfile5 = open('C://Users//Esri//Desktop//statistics//uheadtongji.txt',"r",encoding='utf-8')
umonth=[]
for line5 in outfile5.read().split('\n'):
    umonth.append(line5[:7])
#print(year)
#print(month)
outfile5.close()
uyemon=[]
for mon in umonth:
    #print(mon)
    outfile6 = open('C://Users//Esri//Desktop//statistics//uheadtongji.txt', "r", encoding='utf-8')
    summ=0
    for line6 in outfile6.read().split('\n'):
        monn=line6[:7]
        if monn==mon:
            summ+=int(line6[11:])
    uyemon.append(summ)
month=[]
for dmonth in umonth:
    if dmonth not in month:
        month.append(dmonth)
print(month)
yemon=[]
for dyemon in uyemon:
    if dyemon not in yemon:
        yemon.append(dyemon)
print(yemon)

i22=0
z22=[]
for c22 in month:
    i22+=1
    if i22!=len(month):
        z22.append(str(c22)+','+str(yemon[i22-1])+'\n')
    else:
        z22.append(str(c22) + ',' + str(yemon[i22 - 1]))
print(z22)
outfile7 = open('C://Users//Esri//Desktop//statistics//monthstatistics.txt', "w", encoding='utf-8')
headms='月份'+','+'次数'+'\n'
outfile7.write(headms)
outfile7.writelines(z22)
outfile7.close()
import xlsxwriter
import re
import datetime
#if not os.path.exists(r'C://Users//Esri//Desktop//statistics//%s.xlsx'%i22):
exc=xlsxwriter.Workbook(r'C://Users//Esri//Desktop//statistics//ArcGIS知乎站内搜索统计%s.xlsx'%re.sub(':','',str(datetime.datetime.now())))
worksheet=exc.add_worksheet()
date_format = exc.add_format({'num_format': 'mmmm d yyyy'})
for row in range(0,len(z22)):
    print(row)
    worksheet.write_row(int(row),0,z22[row].replace('\n','').split(','))
    # worksheet.write(row, 0,z22[row].replace('\n','').split(',')[0],date_format)
    # worksheet.write(row, 1, int(z22[row].replace('\n', '').split(',')[1]))
exc.close()