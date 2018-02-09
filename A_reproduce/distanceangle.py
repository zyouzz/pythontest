#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'

import arcpy
import math

popath=r"D:\test\test.gdb\testsoatial\point"
xyfield = ["SHAPE@X","SHAPE@Y"]
pointGeometryList = []

with arcpy.da.SearchCursor(popath, xyfield) as cursor:
    for row in cursor:
        #以方位角45度（math.pi/4）为例，计算出新的坐标
        newx=row[0]+5000*math.cos(math.pi/4)
        newy=row[1]+5000*math.sin(math.pi/4)
        pointGeometry = arcpy.PointGeometry(arcpy.Point(newx,newy))
        pointGeometryList.append(pointGeometry)
arcpy.env.outputCoordinateSystem = arcpy.Describe(popath).spatialReference#输出的坐标系统与原始点数据相同
arcpy.Buffer_analysis (pointGeometryList,  "D:/test/test.gdb/buffercircle",5000)