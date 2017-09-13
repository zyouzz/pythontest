#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import arcpy
import os
#
file=r'D:\test\test.gdb\point1017'
newfile=arcpy.CopyFeatures_management(file)
print newfile
for finame in arcpy.ListFields(newfile):
    print finame.name