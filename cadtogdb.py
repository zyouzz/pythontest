#!/usr/bin/env python
# -*-coding:utf-8 -*-
# __author__ = 'jiang'
# -*- coding: UTF-8 -*-
import arcpy

arcpy.env.workspace = r'D:\test\ArcTutor\CAD'
#input_cad_dataset = r"D:\10.3tutor\ArcTutor\CAD\CAD_append\cad_dwg"
out_gdb_path = r'D:\test\ArcTutor\CAD\cadtogdb.gdb'


reference_scale = "1000"
spatial_reference = "NAD_1983_StatePlane_Kansas_North_FIPS_1501_Feet"
out_dataset_name = "all_cad"

datasetlist = arcpy.ListDatasets("*", "Feature")
vTab = []
for fd in datasetlist:
    # vTab.append(fd)
    print fd
    arcpy.CADToGeodatabase_conversion(fd, out_gdb_path, str(fd)[:-4], reference_scale)