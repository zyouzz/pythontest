#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import arcpy
import os
from arcpy import env
env.workspace = "C:/Users/Esri/Desktop/GFF_Data"
outworkspace = "D:/test/test.gdb"
fclist = arcpy.ListFeatureClasses()
for shapefile in fclist:
    fcname = arcpy.Describe(shapefile).basename
    newfcname = arcpy.ValidateTableName(fcname)
    outfc = os.path.join(outworkspace, newfcname)
    arcpy.CopyFeatures_management (shapefile, outfc)


def type(a):
    if a=="耕地":
        return 1
    elif a=="林地":
        return 2
    elif a=="草地":
        return 3
    elif a=="城乡工矿居民用地":
        return 4
    elif a=="水域":
        return 5
    elif a=="未利用地":
        return 6
