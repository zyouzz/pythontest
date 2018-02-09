#!/usr/bin/env python
# -*-coding:utf-8 -*-
#__author__ = 'jiang'

import arcpy
mxd = arcpy.mapping.MapDocument('D:/test.mxd')
df = arcpy.mapping.ListDataFrames(mxd)[0]
lyrs = arcpy.mapping.ListLayers(mxd)[0]
df.spatialReference=arcpy.Describe(lyrs).spatialReference
mxd.save()
del mxd