#!/usr/bin/env python
#-*-coding:utf-8 -*-
__author__ = 'jiang'
#coding=gbk
##修改label的显示字段
import arcpy
mxd = arcpy.mapping.MapDocument(r"C:\Users\Esri\Desktop\test.mxd")
df = arcpy.mapping.ListDataFrames(mxd)
for dataframe in df:
    da=dataframe.name
    print da
    lyname=arcpy.mapping.ListLayers(mxd, "", dataframe)
    for lyrname in lyname:
         #print lyrname.name
         if lyrname.name == "广州市各区":
             lyrname.name = "point1"
mxd.save()
del mxd
sd=arcpy.mapping.ListDataFrames()


