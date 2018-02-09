#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import pandas as pd
import jieba
import os
import sys
import collections
#reload(sys)
#sys.setdefaultencoding('utf-8')

sear=pd.read_excel(r'C:\Users\Esri\Desktop\statistics\爬取的数据源.xlsx')
# print(sear['搜索关键词'].value_counts()[:100])
# word='土地覆被作为GIS基础的数据，在应用研究中具有很重要的地位，毕竟我们大部分从事于“地球表面”的工作。做过影像分类的同学或许都会有这么个感受：一般情况下，现有的自动分类结果大部分简直不忍直视，如果人工目视解译，却又是一个大工程，费时费力。如今各种技术热点层出不穷，是否有解决之道呢？有一句老话说“他山之石，可以攻玉”，微软作为全球IT行业的先行者，在近年来的人工智能方面也做的极为出色。于是，Esri与其通力合作，将微软的人工智能技术集成到ArcGIS产品中，借助云端服务器的能力，实现了惊人的效率。'

# print(','.join(jieba.cut(sear['搜索关键词'])))
# print(sear['搜索关键词'].astype('str').map(str.lower).value_counts()[:100])
# pd.DataFrame(sear)['搜索关键词'].astype('str').map(str.lower).value_counts()[:100].to_excel(r'C:\Users\Esri\Desktop\statistics\爬取的数据源11.xlsx')
# print((pd.DataFrame(sear)[pd.DataFrame(sear).搜索关键词.astype('str').map(str.lower).str.contains('arcgis')])['搜索关键词'].value_counts())
liw=(pd.DataFrame(sear)[pd.DataFrame(sear).搜索关键词.astype('str').map(str.lower).str.contains('arcgis')])['搜索关键词']
ssss=','.join(liw).split(',')
xxx=[]
for mm in liw:
    ll=mm[mm.lower().find('arcgis'):mm.lower().find('arcgis')+6]
    xxx.append(ll)
sll=len(liw)
print(sll)
coo=collections.Counter(xxx)
print(coo)
zdd={key:coo[key] for key in coo}
nd=sorted(zdd.items(), key=lambda e:e[1], reverse=True)
print(nd)
for key in nd:
    print('%s(%d次)%s'%(key[0],key[1],str(round((key[1]/sll)*100,2))+'%'))