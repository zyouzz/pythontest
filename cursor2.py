import arcpy
routep="D:\\test\\test.gdb\\point"
#cursor=arcpy.da.SearchCursor(routep,['num','time'])
with arcpy.da.SearchCursor(routep,['num','time']) as cursor:
    for row in cursor:
        print(row)
