#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import arcpy
ca=r"D:\test\test.gdb\ca"
codeblock="""def Glare_Rating(fieldvalue):
    if fieldvalue <0 or fieldvalue >75:
        Glare_characteristics = "Glare free zone"
    elif 0<fieldvalue and fieldvalue<14:
        Glare_characteristics = "Very strong"
    elif 14<fieldvalue and fieldvalue<30:
        Glare_characteristics = "strong"
    elif 30<fieldvalue and fieldvalue<10005:
        Glare_characteristics = "Moderate"
    else:
        Glare_characteristics = "weak"
    return Glare_characteristics"""
arcpy.CalculateField_management(ca, "texttest","Glare_Rating(!trim!)", "PYTHON_9.3",codeblock)