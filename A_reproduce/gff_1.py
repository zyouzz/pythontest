#!/usr/bin/env python
# -*-coding:utf-8 -*-
import arcpy
import numpy
# import os
# Get input Raster properties
inputRaster = arcpy.Raster('D:/GuoFangfang/Newphytologist-requirements/TrendProject.gdb/Gri20100725_Clip1_Clip')

mycellH = inputRaster.meanCellHeight
mycellW = inputRaster.meanCellWidth
lowerLeft = arcpy.Point(inputRaster.extent.XMin,inputRaster.extent.YMin)


list_inci = []
for i in range (1,552 ):
    for j in range (1,632):
         MyX = inputRaster.extent.XMin + i* mycellW
         Inci = -6.12996E-8*MyX + 1.23039
         list_inci.append(Inci)
arrInci = numpy.array(list_inci)
arrInci.shape = (551,631)

MyRaster20100725 = arcpy.NumPyArrayToRaster(arrInci,lowerLeft,mycellW,mycellH,value_to_nodata =100)

MyRaster20100725.save("D:/GuoFangfang/Newphytologist-requirements/Gri")

