#!/usr/bin/env python
#-*-coding:utf-8 -*-
__author__ = 'jiang'
import os
import os.path
import re
import urllib.parse
import datetime
starttime = datetime.datetime.now()
rootdir ="C:\\Users\\Esri\\Desktop\\log"
# 指明被遍历的文件夹
#遍历日志文件夹下的日志文件
file1 = open('C://Users//Esri//Desktop//log.txt', 'a')
line1 ="IP"+ ',' + "日期"+ ',' + "搜索关键词"+ '\n'

# 对象file的write方法将字符串line写入file中.1point3acres缃�
file1 = file1.write(line1)
file2 = open('C://Users//Esri//Desktop//tongji.txt', 'a')
line2 ="日期"+ ',' + "次数"+ '\n'
file2 = file2.write(line2)
for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    # print(parent)
    # # for dirname in dirnames:
    # #     print(dirname)
    # # for filename in filenames:
    # #     print(filename)
    # # for dirname in  dirnames:                       #输出文件夹信息
    # #     print("parent is:" + parent)
    # #     print("dirname is" + dirname)
    # #
    day = 1
    i=1
    for filename in filenames:                        #输出文件信息
        # print("parent is:" + parent)
        # print("filename is:" + filename)

        filedate=filename[7:-4]
        filepath=os.path.join(parent,filename)
        print(filedate)
        print(filepath)
        #print("the full name of the file is:" + os.path.join(parent,filename)) #输出文件路径信息
        #读取日志文件
        input = open(filepath, 'r')
        # rangeUpdateTime = [0.0]
        num=1
        for line in input:
            # print(line)

            # line = line.split()

            if ('GET //search/ajax/search_result/search_type-questions__q-' and 'template-__page-1' and 'search_type-questions') in line:
                 kw1=line.split()[6][53:-19]
                 kw=urllib.parse.unquote(kw1).replace('_','')
                 if  '?' in kw:
                     pass
                 else:

                     # try:
                     #    kw=bytes.fromhex(keyword.replace('%', '')).decode('utf-8')
                     #    i+=1
                     # except:
                     #    print(line.split()[0] + " " + line.split()[3][1:] + " " + keyword)
                     #    continue
                     #    i+=1
                     # print(line.split()[0]+" "+line.split()[3][1:]+" "+kw)
                     file1 = open('C://Users//Esri//Desktop//log.txt', 'a')
                     line1 = str(line.split()[0]) + ',' + str(line.split()[3][1:])+','+ kw+ '\n'
                     file1 = file1.write(line1)
                     # print(i)
                     i+=1
                     num+=1

        day+=1
        print(filedate+":共有"+str(num)+"次搜索")
        file2 = open('C://Users//Esri//Desktop//tongji.txt', 'a')
        line2 = filedate + ',' + str(num)+ '\n'
        file2 = file2.write(line2)
day-=1
i-=1
# print(filenames[0][7:-4]+","+filenames[1][7:-4]+","+filenames[2][7:-4])
print(str(day)+"天一共有："+str(i)+"次搜索")
endtime = datetime.datetime.now()
time = (endtime - starttime).seconds
print("用时"+str(time)+"秒")
