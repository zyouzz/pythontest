#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import arcpy
mxd = arcpy.mapping.MapDocument(r'C:\Users\Esri\Desktop\test1.mxd')
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
lyr = arcpy.mapping.ListLayers(mxd)[0]
lyrFile = arcpy.mapping.Layer(r"D:\test\测试数据\p114r075_7k20000501_z50_nn61.tif.lyr")
arcpy.mapping.UpdateLayer(df, lyr, lyrFile, True)
if lyr.symbologyType == "RASTER_CLASSIFIED":
  lyr.symbology.reclassify()
arcpy.RefreshTOC()
arcpy.RefreshActiveView()
arcpy.mapping.ExportToJPEG(mxd, (r"C:\\Users\\Esri\Desktop\test67766.jpg"),resolution=350)