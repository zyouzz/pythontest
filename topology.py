# -*- coding:utf-8 -*-
#导入所需的开发包
import arcpy
from arcpy import env
import datetime
import numpy

#设置数据库环境
gdbpath = "E:/SpatialAnalysis.gdb"
env.workspace = gdbpath #().decode('utf8')

#设置计算重叠的

featureclass = gdbpath + "/"+ "AAA_Feature"

#从要素表获取过滤后的要素对象
features = []

expression = "OBJECTID" + ' > -1'



#获得准备处理的记录集
rows = arcpy.da.SearchCursor(featureclass, ["SHAPE@"], where_clause=expression)
for row in rows:
# print row
geo = row[0]
if row == None or geo == None:
print row[1] + "--- None"
continue
# print row[1] #+ "---" + geo
if row is not None and geo.extent is not None :
extent = geo.extent
# print("Extent of Name {0}:".format(row[1]))
# print("XMin: {0}, YMin: {1}".format(extent.XMin, extent.YMin))
# print("XMax: {0}, YMax: {1}".format(extent.XMax, extent.YMax))
features.append(row)

# 存储有关系的矿权集合

fields = ("SHAPE@")
outFeatureClass = featureclass + "_overlaps3"
cursor = arcpy.da.InsertCursor(outFeatureClass, fields)
SR = arcpy.Describe(featureclass).spatialReference

#计算当前的要素与其他要素的空间关系
count = len(features)
for i in range(0 , count):
    geometry1 = features[i][0]
        for j in range(i+1 , count):
            geometry2 = features[j][0]
            kqid1 = features[i][1]
            kqid2 = features[j][1]
            b1 = geometry1.overlaps(geometry2) #基础几何是否与比较几何"重叠"
# b2 = geometry1.equals(geometry2) #指示原几何和参照几何的 shape 类型是否相同并在平面中定义相同点集
            dist = geometry1.distanceTo(geometry2) #两个集合之间的距离
            b3 = dist == 0
# b4 = geometry1.touches(geometry2) #基础几何是否与比较几何"接触"
# b5 = geometry1.crosses(geometry2) #基础几何是否与比较几何"交叉"--多边形和多边形不存在这类关系
            b6 = geometry1.disjoint(geometry2) #基础几何是否与比较几何不相交
            b7 = geometry1.contains(geometry2) # 基础几何是否与比较存在包含关系
            print str(i) + "--" + str(j) + "--" + kqid1 + " -- " + kqid2 + " --- " + str(dist)
            if b1:
                print kqid1 + " -- " + kqid2 + " -- OK "
                cursor.insertRow((geometry1))

                del cursor
                print 'Over....'
-----------------------------------------------------------------------------------------------
核心是此处：
b1 = geometry1.overlaps(geometry2) #基础几何是否与比较几何"重叠"
# b2 = geometry1.equals(geometry2) #指示原几何和参照几何的 shape 类型是否相同并在平面中定义相同点集
dist = geometry1.distanceTo(geometry2) #两个集合之间的距离
b3 = dist == 0
# b4 = geometry1.touches(geometry2) #基础几何是否与比较几何"接触"
# b5 = geometry1.crosses(geometry2) #基础几何是否与比较几何"交叉"--多边形和多边形不存在这类关系
b6 = geometry1.disjoint(geometry2) #基础几何是否与比较几何不相交
b7 = geometry1.contains(geometry2) # 基础几何是否与比较存在包含关系

