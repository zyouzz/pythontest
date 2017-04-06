#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = r"D:\preset\培训素材\ArcGIS高级制图培训\1-培训数据\3-地图数据符号化\3-地图数据符号化\Demo2_山体阴影晕渲\Data_Yosemite\Data_Elev"

# Set local variables
inRaster = "dem.tif"
inMaskData = "New_Shapefile.shp"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute ExtractByMask
outExtractByMask = ExtractByMask(inRaster, inMaskData)

# Save the output
outExtractByMask.save(r"D:\preset\培训素材\ArcGIS高级制图培训\1-培训数据\3-地图数据符号化\3-地图数据符号化\Demo2_山体阴影晕渲\Data_Yosemite\Data_Elev\extractmask")
