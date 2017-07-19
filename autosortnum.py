#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import arcpy
arcpy.env.workspace = r"D:/test/test.gdb"
point='tesst/mmm'
outname=point.split('/')[1]+'sort5'
outpath=point.split('/')[0]+'/'+outname
outpath1=outpath+'5'
arcpy.CopyFeatures_management(point, outpath)
arcpy.AddXY_management(outpath)
ASCENDING="ASCENDING"
DESCENDING="DESCENDING"
sortfield=[["POINT_X", ASCENDING],[ "POINT_Y", DESCENDING]]
arcpy.Sort_management(outpath,outpath1,sortfield)
arcpy.AddField_management(outpath1,'paixu','DOUBLE')
arcpy.CalculateField_management(outpath1, "paixu",'!OBJECTID!', "PYTHON_9.3")

# with arcpy.da.UpdateCursor(outpath1,["paixu"]) as cursor:
#     id=1
#     for row in cursor:
#         row[0]=id
#         cursor.updateRow(row)
#         id+=1
# with arcpy.da.UpdateCursor(outpath,['POINT_X', 'POINT_Y']) as cursor:
#     for cur in cursor:
#         print cur
    # for row in arcpy.da.SearchCursor(outpath, ["SHAPE@XY"]):
    #     print row[0][0]
    #     liebiao.append(row[0])
# liebiao.sort(key=lambda liebiao:liebiao[0], reverse=False)
# liebiao.sort(key=lambda x:(x[0],x[1]))
# print liebiao
# spatial_reference = arcpy.Describe(point).spatialReference
# outname=point.split('/')[1]+'sort'
# outpath=point.split('/')[0]+'/'+outname
# arcpy.CreateFeatureclass_management(out_path='tesst', out_name=outname,geometry_type="POINT",template=point,spatial_reference=point)
# cursor = arcpy.da.InsertCursor(outpath, ["SHAPE@XY"])
# for corr in liebiao:
#     print corr
#     cursor.insertRow([corr])
    # x,y=row[0]
    # print("%f,%f "%(x, y))
