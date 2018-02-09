#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import arcpy
import numpy as np
array=np.empty((100,100),dtype=np.uint8)
ss=arcpy.NumPyArrayToRaster(array,arcpy.Point(8176604.745000,2056698.244800),x_cell_size=20,y_cell_size=20)
rray=np.empty((100,100),dtype=np.int8)
dd=arcpy.NumPyArrayToRaster(rray,arcpy.Point(8176604.745000,2056698.244800),x_cell_size=20,y_cell_size=20)
zrray=np.empty((100,100),dtype=np.uint8)
ee=arcpy.NumPyArrayToRaster(zrray,arcpy.Point(8176604.745000,2056698.244800),x_cell_size=20,y_cell_size=20)