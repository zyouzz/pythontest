# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Pretreatment.py
# Created on: 2016-09-22
#   (generated
# Description:。
# Import arcpy module
import os
import arcpy
inputDir = "C:\\Users\\Esri\\Desktop\\testdata"
Output = "C:\\Users\\Esri\\Desktop\\new"
arcpy.env.workspace = "C:\\Users\\Esri\\Desktop\\testdata"
workspacess = arcpy.ListWorkspaces("*","Access")
for workspace in workspacess:
    asss = workspace.split("\\")[-1]
    arcpy.CreatePersonalGDB_management(Output, asss)
    dimao=os.path.join(workspace,u"地貌")
    walk = arcpy.da.Walk(dimao, datatype="FeatureClass")
    for root, dirs, files in walk:
        for f in files:
            fc=os.path.join(dimao,f)
            out_data =os.path.join(Output,asss,f)
            arcpy.Copy_management(fc, out_data)
print("处理完成")
