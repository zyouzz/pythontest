#!/usr/bin/env python
#-*-coding:utf-8 -*-
__author__ = 'jiang'
f3line=open('C://Users//Esri//Desktop//statistics//tongji.txt',"r+").read().split()
f4= open('C://Users//Esri//Desktop//statistics//uheadtongji.txt', 'w')
i=0
for li in f3line:
    i+=1
#print(i)
num=1
for line3 in f3line:
    f4 = open('C://Users//Esri//Desktop//statistics//uheadtongji.txt', 'a')
    #print(line3)
    if line3=='日期,次数':
        pass
    else:
        if num != i:
            f4.write(line3+'\n')
        else:
            f4.write(line3)
    num+=1
# f5= open('C://Users//Esri//Desktop//statistics//uheadtongji.txt', 'r').read().replace('\n',',').split(',')
# i=1
# xbeta= []
# y= []
# for uh in f5:
#     print(uh)
#     if i%2 !=0:
#         xbeta.append(uh)
#     else:
#         y.append(int(uh))
#     i+=1
# x=xbeta[:len(xbeta)-1]
# print(x)
# print(y)
#
# '''成图'''
#
# i=1
# x1=[]
# for i in range(1,len(x)+1):
#     x1.append(int(i))
# DataX =tuple(x1)
# #print(type(DataX))
# DataY =tuple(y)
# #print(type(DataY))
# fig1 = plt.figure()
# fig1.set_size_inches(30, 10.5)
# rects=plt.bar(left = DataX,height = DataY,width = 0.5,align="center",yerr=0.000001,facecolor = 'lightskyblue',edgecolor = 'white')
# def autolabel(rects):
#     for rect in rects:
#         height = rect.get_height()
#         plt.text(rect.get_x()+rect.get_width()/3., 1.01*height, '%s' % int(height),color='red',fontsize=25)
# autolabel(rects)
# plt.xlabel('日期',fontsize=20)
# plt.ylabel('次数',fontsize=20)
# plt.title('ArcGIS知乎站内搜索每天统计（2016-06-16至'+filedate+'）'+'\n'+'('+str(day)+"天一共有："+str(sumday)+"次搜索)",fontsize=26)
# plt.yticks(fontsize=16)
# plt.xticks(DataX,tuple(x),fontsize=16)
# saveday="C:/Users/Esri/Desktop/"+re.sub(':','',str(datetime.datetime.now()))+".png"
# #print(savename)
# fig1.savefig(saveday, dpi=100)
# #plt.show()
# file5.close()