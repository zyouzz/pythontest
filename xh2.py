#coding:utf-8
'''
使用循环嵌套判断然后进行spatial join,
PS:接触Arcpy没多长时间，用有限的水平写的，可能有更好的实现方式，以下仅供参考
'''
import arcpy
import os
arcpy.env.workspace = r"D:\test\trans\station.gdb"#存储站点gdb的路径
station = arcpy.ListFeatureClasses()
line=r"D:\test\trans\line.gdb"
outspace=r"D:\test\New File Geodatabase.gdb"#输出到该gdb的路径
linewalk=arcpy.da.Walk(line, datatype="FeatureClass")#
'''由于arcpy.ListFeatureClasses()只能是一个工作空间，为了嵌套比较，
所以用了arcpy.da.Walk,实际arcpy.da.Walk可以用两次，不用arcpy.ListFeatureClasses()'''
for dirpath, dirnames, filenames in linewalk:#获取线的名称和路径
    for linename1 in filenames:#获取线的名字
        linename=linename1[4:]#将线名之前“line”去掉，以便下边的线路和站点判定
        for stationpath in station:#同样获取站点路径
            stationname=os.path.splitext(stationpath)[0]#获取站点名
            if linename==stationname:#判断线路和站点名字是否一致
                    linepath=os.path.join(line, linename1)#线路路径
                    outfc=os.path.join(outspace, linename)#站点路径
                    arcpy.SpatialJoin_analysis(linepath, stationpath, outfc)#spatial join!
print u"处理完成"