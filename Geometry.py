import arcpy
from arcpy import env
env.workspace="C:/data"
arcpy.CreateFileGDB_management("C:/output","polygon.gdb")
spatial_reference=arcpy.Describe("D:\\test\ArcTutor\Spatial Analyst\Stowe.gdb\elevation").spatialReference
arcpy.CreateFeatureclass_management("C:/output/polygon.gdb","polyg","polyline","C:\Users\Esri\Documents\ArcGIS\Default.gdb\elevation_RasterDomain","DISABLED","DISABLED",spatial_reference)
rt= arcpy.GetRasterProperties_management("D:\\test\ArcTutor\Spatial Analyst\Stowe.gdb\elevation","TOP")
rb= arcpy.GetRasterProperties_management("D:\\test\ArcTutor\Spatial Analyst\Stowe.gdb\elevation","BOTTOM")
rl= arcpy.GetRasterProperties_management("D:\\test\ArcTutor\Spatial Analyst\Stowe.gdb\elevation","LEFT")
rr= arcpy.GetRasterProperties_management("D:\\test\ArcTutor\Spatial Analyst\Stowe.gdb\elevation","RIGHT")

zs=(rl,rt)
zx=(rl,rb)
ys=(rr,rt)
yx=(rr,rb)
fc="C:/output/polygon.gdb/polyg"
cursor = arcpy.da.InsertCursor(fc, ["SHAPE@XY"])
array=arcpy.array([arcpy.point(zs),arcpy.point(zx)，arcpy.point(ys)，arcpy.point(yx)])
polyline=arcpy.Polyline(array)
cursor.insertrow(polyline)
#cursor.insertRow([xy])
#cursor.insertRow([zx])
#cursor.insertRow([ys])
#cursor.insertRow([yx])

