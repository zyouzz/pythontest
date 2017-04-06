#!/usr/bin/env python
#-*-coding:utf-8 -*-
__author__ = 'jiang'
import arcpy
mxd = arcpy.mapping.MapDocument(r"C:\Users\Esri\Desktop\test.mxd")
for lyr in arcpy.mapping.ListLayers(mxd):
     if lyr.name == "广州市各区":
        lyr.name = "point1"
mxd.save()
del mxd