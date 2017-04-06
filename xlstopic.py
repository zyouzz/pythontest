#!/usr/bin/env python
# -*-coding:utf-8 -*-
#__author__ = 'jiang'
import  xlrd
from numpy import *
import matplotlib.pyplot as plt
import numpy as np
top100=xlrd.open_workbook(r'C:\Users\Esri\Desktop\statistics\关键词top100.xlsx')
try:
    topsheet=top100.sheet_by_name('Sheet1')
except:
    print('no sheet in xlsx named Sheet1')
nrows=topsheet.nrows
ncols=topsheet.ncols
col1=[]
col2=[]
filters=['for','not','to','be','the','is','in','a','create','no']
num=1
for i in range(1,nrows):
    row_data=topsheet.row_values(i)
    if row_data[0] not in filters:
        col1.append(row_data[0])
        col2.append(int(row_data[1]))
        num+=1
print(num)
print(col1)
print(col2)
##为了方便展示，翻转一下关键词和次数，
keyw=tuple(reversed(col1))
col3=[]
##翻转函数reversed()结果是一个迭代，需要重新创建list
for sornew in reversed(col2):
    col3.append(sornew)
data=np.array(col3)
x=np.arange(len(col1))
fig=plt.figure()
fig.set_size_inches(20, 30)
ax1=plt.axes([0.07,0.03,0.9,0.93])
area=ax1.barh(x,data,align='center',color='g',alpha=0.5)
plt.ylim(-1,num)
plt.xlabel('data',size=18,color='k')
ax1.set_yticks(x)
ax1.set_yticklabels(keyw)
plt.xlabel('次数', fontsize=23)
plt.ylabel('关键词', fontsize=23)
plt.title('ArcGIS知乎站内搜索关键词统计',fontsize=30)
###加标注
def autolabel(area):
    numm = 1
    for rect1 in area:
        height = rect1.get_width()
        print(int(height))
        #plt.text(rect1.get_x() + rect1.get_width() / 3., 1.01 * height, '%s' % int(height), color='red', fontsize=25)
        plt.text(height+1,  numm-1, '%s' % int(height), color='red')
        numm+=1


autolabel(area)

fig.savefig(r'C:\Users\Esri\Desktop\top100.png', dpi=100)




