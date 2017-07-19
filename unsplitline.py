#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
# -\*- coding: utf-8 -\*-
import arcpy
RasterT_CostPat2 = "J:\\\\arcgis\\\\ArcTutor\\\\Spatial Analyst\\\\Stowe.gdb\\\\RasterT_CostPat2"
road5= r"J:\\\\arcgis\\\\ArcTutor\\\\Spatial Analyst\\\\Stowe.gdb\\\\road5"
arcpy.AddField_management(RasterT_CostPat2,"SIGH","TEXT")
start=9001
to=9002
sigh = str("from%dto%d" % (start, to))
print sigh
arcpy.CalculateField_management(RasterT_CostPat2, "SIGH", "\'%s\'"%sigh, "PYTHON_9.3")  # 字段计算器
arcpy.UnsplitLine_management(RasterT_CostPat2,road5,["grid_code","SIGH"])