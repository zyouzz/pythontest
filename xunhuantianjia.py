#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import random
def genenum():
    ll=[]
    for num in range(10):
        ll.append(num)
    return ll
sz=genenum()
# print sz
while cc<90:
    for shuzi in sz:
        globals(cc)
        if shuzi<=6:
            sz.remove(shuzi)
        if len(sz)<=6:
            sz = genenum()
            cc=random.randint(1,100)
            print cc






