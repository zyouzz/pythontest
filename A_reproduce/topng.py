#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'

import arcpy

# 导出图片mxdPath：mxd地图路径，
# 初始的mxd文件
mxdpath = r'C:\Users\Esri\Desktop\sss1.mxd'
mxd = arcpy.mapping.MapDocument(mxdpath)
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
curLayer = arcpy.mapping.ListLayers(mxd, "", df)[0]
df.extent = curLayer.getExtent()
interIMG = r'd:\test55.png'
# arcpy.mapping.ExportToPNG(mxd, interIMG, "PAGE_LAYOUT",df_export_width=curLayer.getExtent().width / 2,
#                           df_export_height=curLayer.getExtent().height / 2,background_color="255,255,255", transparent_color="255,255,255",world_file=True,interlaced='False')  # 导出数据视图

arcpy.mapping.ExportToPNG(mxd, interIMG, resolution=350, background_color="255,255,255", transparent_color="255,255,255")  # 导出布局视图
del mxd
# del df
