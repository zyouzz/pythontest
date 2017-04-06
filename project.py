#coding:utf-8
import arcpy
import os
arcpy.env.workspace = "C:\\Users\\Esri\\Desktop\\test__20160919\\qian\\CODE1.gdb"
arcpy.env.overwriteOutput = True
outWorkspace = "C:\\Users\\Esri\\Desktop\\test__20160919\\hou\\CODE1.gdb"
#from arcpy import env
#from arcpy import interop
#arcpy.ImportToolbox("Model Functions")
#path="C:\\Users\\Esri\\Desktop\\test__201609191\\qian"

#for filename in os.listdir(path):
   # arcpy.CreateFileGDB_management("C:\\Users\\Esri\\Desktop\\test__201609191\\hou",filename)
featureclasses = arcpy.ListFeatureClasses()
for fcname in featureclasses:
    #fcpath="C:\\Users\\Esri\\Desktop\\test__20160919\\qian\\CODE1.gdb\\"+fcname
    outfea = os.path.join(outWorkspace, fcname)
    arcpy.Project_management(fcname,outfea,"PROJCS['CGCS2000_GK_CM_117E',GEOGCS['GCS_China_Geodetic_Coordinate_System_2000',DATUM['D_China_2000',SPHEROID['CGCS2000',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',117.0],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", "", "GEOGCS['GCS_China_Geodetic_Coordinate_System_2000',DATUM['D_China_2000',SPHEROID['CGCS2000',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")
