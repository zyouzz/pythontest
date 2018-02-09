#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import arcpy

arcpy.env.workspace = "C:/Users/Esri/Desktop/GFF_Data"
import glob
def defproj(file):
     infc = file
     sr = arcpy.SpatialReference(4326)
     arcpy.DefineProjection_management(infc, sr)

def Read_file(mydir):
    list_dir = glob.glob(mydir)
    for i in list_dir:
         defproj(i)

if __name__ == '__main__':
   mydir = 'C:/Users/Esri/Desktop/GFF_Data/*.shp'

   Read_file(mydir)