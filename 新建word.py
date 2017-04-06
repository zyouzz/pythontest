#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
with open(r'C:\Users\Esri\Desktop\新建文本文档.txt','r') as f:
    # print(f.read())
    for name in f.read().split('\n'):
        file=open(r'C:\Users\Esri\Desktop\白皮书整理\%s.doc'%name,'w')
        file.close()


