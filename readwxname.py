#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'

with open(r'D:\vv.txt') as txt1:
    lines=txt1.readlines()
    i=1
    for line in lines:
        if i%4==1:
            print line.replace('\n','')
        i += 1