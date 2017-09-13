#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import arcpy
def getsde(sdepath):
    desc = arcpy.Describe(sdepath)
    print desc
    cp = desc.connectionProperties.instance
    return cp
