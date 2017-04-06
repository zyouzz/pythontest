# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Pretreatment.py
# Created on: 2016-09-22
#   (generated
# Description:。
# ---------------------------------------------------------------------------

# Import arcpy module
import os
import arcpy
from arcpy import env

#env.workspace = inputDir
inputDir = r"C:\Users\Esri\Desktop\testdatadata"
input_data =unicode(inputDir, "utf-8")

Output = r"C:\Users\Esri\Desktop\output"
arcpy.env.workspace = r"C:\Users\Esri\Desktop\output"
# 加速处理设置
arcpy.env.parallelprocessingFactor = "100%"
arcpy.env.overwriteOutput = True

def FCAlterAliasname(rootDir):
    # filter folder

    workspacess = arcpy.ListWorkspaces("*", "Access")
    for workspace in workspacess:
        mdbname=workspace.split("\\")[-1]
        arcpy.CreatePersonalGDB_management(Output, mdbname)
        x = 0
        for root, dirs, files in os.walk(rootDir):
            for f in files:
                #print os.path.join(root, f)
                filetype = os.path.splitext(f)[1]
                if filetype == ".mdb":
                    env.workspace = os.path.join(root, f)
                    #print env.workspace
                    x = x + 1
                    print ("----------开始处理第 {0} 个 {1} 文件-----------".format(x,f))
                    if arcpy.Exists("TERL"):

                        in_data = env.workspace + os.sep + u"地貌" + os.sep + "TERL"
                        print in_data

                        out_data = Output + os.sep + f
                        print out_data

                        arcpy.Copy_management(in_data, out_data)

print u"处理完成"
if __name__ == '__main__':
    FCAlterAliasname(input_data)