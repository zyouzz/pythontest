import arcpy
routep=r"D:\\test\\test.gdb\\polyline"
cursor=arcpy.da.InsertCursor(routep,['roadID','distance'])
for i in range(0,25):
    cursor.insertRow([i,100])