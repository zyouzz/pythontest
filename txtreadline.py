#!/usr/bin/env python
#-*-coding:utf-8 -*-
#__author__ = 'jiang'
oline=0
for linex in open('C://Users//Esri//Desktop//statistics//log.txt','r',encoding='utf-8').read().split('\n'):
    oline+=1
print(oline)
linenum=0
li=[]
open('C://Users//Esri//Desktop//log121212.txt','w',encoding='utf-8')
for line in open('C://Users//Esri//Desktop//statistics//log.txt','r',encoding='utf-8').read().split('\n'):
    linenum += 1
    if line !='' and linenum !=oline-1:
        li.append(line + '\n')
    else:
        if linenum ==oline-1 :
        #print(line)
            li.append(line)
        else:
            pass
#print(li)
open('C://Users//Esri//Desktop//log121212.txt', 'a', encoding='utf-8').writelines(li)