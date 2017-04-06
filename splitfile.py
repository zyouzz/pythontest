#!/usr/bin/env python
#-*-coding:utf-8 -*-
# __author__ = 'jiang'
import os
open6=open('C://Users//Esri//Desktop//access_2016-07-06.log', 'r').read().split('\n')
ospath='C:/Users/Esri/Desktop/assc/access_2016-07-'
i=6
for o6 in open6:
    try:
        day = o6.split()[3].replace('[', '')[0:2]
        print(day)
        path = ospath + str(day.zfill(2)) + '.log'
        print(path)
        f = open(path, 'a')
        print(o6)
        if int(day)==i:
            f.write(o6+'\n')
            #print(o)
        else:
            i+=1
            f.write(o6 + '\n')
    except:
        break
    # i+=1
    # print(i)
    # if int(i)!=19:
    #     continue

