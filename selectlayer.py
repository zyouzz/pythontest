#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import arcpy
oid=2
arcpy.MakeFeatureLayer_management("D:\\test\\test.gdb\\cscs200120", "ccf")
arcpy.SelectLayerByAttribute_management("ccf",  "NEW_SELECTION",  ' "OBJECTID" = %d'%oid)