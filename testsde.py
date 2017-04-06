#!/usr/bin/env python
# -*-coding:utf-8 -*-
#__author__ = 'jiang'
import arcpy
arcpy.CheckOutExtension("Spatial")
outRas=arcpy.Raster(r'C:\Users\Esri\Desktop\top100.png')
outRas=outRas+100
outRas.save(r'C:\Users\Esri\AppData\Roaming\ESRI\Desktop10.5\ArcCatalog\Connection to 192.168.220.131.sde\ww23')