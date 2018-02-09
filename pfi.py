#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'

import arcpy

fc = r'D:\test\test.gdb\ces'
queryResult = arcpy.da.SearchCursor(fc,['A','SHAPE@'])

for ll in queryResult:
    print ll[0],ll[1].type