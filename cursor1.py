import arcpy
import datetime
#Create an insert for a table specifying the fields thar will have values provided
fields=['ID','date']
cursor=arcpy.da.InsertCursor('D:\\test\\test.gdb\\polyline',fields)

#Create 25 new rows. Set Default values on distance and CFCC code
for x in range(0,5):
    cursor.insertRow((x*2,datetime.datetime.now()))

# Delete cursor object
del cursor