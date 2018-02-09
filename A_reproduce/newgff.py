import arcpy
import numpy
import os
# Get input Raster properties
inputRaster = arcpy.Raster('D:/GuoFangfang/Newphytologist-requirements/TrendProject.gdb/testnum')
bandno = inputRaster.bandCount
myheight = inputRaster.height
mywidth = inputRaster.width
myextent = inputRaster.extent
mycellH = inputRaster.meanCellHeight
mycellW = inputRaster.meanCellWidth
MyH = mycellH * myheight
MyW = mycellW * mywidth
lowerLeft = arcpy.Point(inputRaster.extent.XMin,inputRaster.extent.YMin)
# print bandno
# print myheight
# print mywidth
# print myextent
# print mycellH
# print mycellW
# print MyH
# print MyW
list_X = []
list_Y = []
list_inci = []
for i in range(1, 250):
    for j in range(1, 250):
         MyX = inputRaster.extent.XMin + i* mycellW
         list_X.append(MyX)
         MyY = inputRaster.extent.YMin + j* mycellH
         list_Y.append(MyY)
         Inci = -6.12996E-8*MyX + 1.23039
         list_inci.append(Inci)
print list_X[:10]
print list_Y[:10]
print list_inci[:10]
arrX = numpy.array(list_X)
arrY = numpy.array(list_Y)
arrInci = numpy.array(list_inci)
XYInci = numpy.concatenate((arrX,arrY,arrInci),axis = 1)
print XYInci[:13]
MyRaster20100725 = arcpy.NumPyArrayToRaster(XYInci,lowerLeft,mycellW,mycellH,value_to_nodata =100)
# MyRaster20100725.save('D:/test/test.gdb/testnum/Gri20100725_trend')

