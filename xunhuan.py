#coding:utf-8
import arcpy
import os
arcpy.env.workspace = "D:\\test"
gdb1="D:\\test\\trans\\line.gdb"
gdb2="D:\\test\\trans\\station.gdb"
outspac="D:\\test\\New File Geodatabase.gdb"
walk1=arcpy.da.Walk(gdb1, datatype="FeatureClass")
walk2=arcpy.da.Walk(gdb2, datatype="FeatureClass")
for dirpath, dirnames, filenames in walk1:
    for filename1 in filenames:
        for path, fnames, namess in walk2:
            for filename2 in namess:
                print(filename2)
                if filename1==filename2:
                    filename3=os.path.join(gdb1, filename1)
                    filename4=os.path.join(gdb2, filename2)
                    outfc=os.path.join(outspac, filename1)
                    arcpy.SpatialJoin_analysis(filename3, filename4, outfc)
                else:
                    print(filename2)