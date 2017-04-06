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
input_data = r"C:\Users\Esri\Desktop\test数据"
input_data =unicode(input_data, "utf-8")
print(input_data)


Output = r"C:\Users\Esri\Desktop\out"
Output =unicode(Output, "utf-8")
print(Output)



# 加速处理设置
arcpy.env.parallelprocessingFactor = "100%"
arcpy.env.overwriteOutput = True

def FCAlterAliasname(rootDir,Output):
    # filter folder
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

                arcpy.CreatePersonalGDB_management(Output, f)

                if arcpy.Exists("TERL"):

                    in_data = env.workspace + os.sep + u"地貌" + os.sep + "TERL"
                    print(in_data)

                    out_data = Output + os.sep + f + os.sep + "TERL"
                    print(out_data)

                    arcpy.Copy_management(in_data, out_data)

                # if arcpy.Exists("TERP"):
                #
                # if arcpy.Exists("TFCA"):
                #
                # if arcpy.Exists("TFCL"):
                #
                # if arcpy.Exists("TFCP"):
                #
                #
                # if arcpy.Exists("TZJN"):
                #
                # if arcpy.Exists("AANP"):
                #
                # if arcpy.Exists("AGNP"):
                #
                # if arcpy.Exists("AZJN"):
                #
                # if arcpy.Exists("CFZL"):
                #
                # if arcpy.Exists("CPTL"):
                #
                # if arcpy.Exists("CPTP"):
                #
                # if arcpy.Exists("CZJN"):
                #
                # if arcpy.Exists("PFZL"):
                #
                # if arcpy.Exists("PIPL"):
                #
                # if arcpy.Exists("PIPP"):
                #
                # if arcpy.Exists("PZJN"):
                #
                # if arcpy.Exists("LFCA"):
                #
                # if arcpy.Exists("LFCL"):
                #
                # if arcpy.Exists("LFCP"):
                #
                # if arcpy.Exists("LFZL"):
                #
                # if arcpy.Exists("LRDA"):
                #
                # if arcpy.Exists("LRDL"):
                #
                # if arcpy.Exists("LRRA"):
                #
                # if arcpy.Exists("LRRL"):
                #
                # if arcpy.Exists("BFZL"):
                #
                # if arcpy.Exists("BOUA"):
                #
                # if arcpy.Exists("BOUL"):
                #
                # if arcpy.Exists("BOUP"):
                #
                # if arcpy.Exists("BRGA"):
                #
                # if arcpy.Exists("BRGL"):
                #
                # if arcpy.Exists("BRGP"):
                #
                # if arcpy.Exists("BZJN"):
                #
                # if arcpy.Exists("RESA"):
                #
                # if arcpy.Exists("RESL"):
                #
                # if arcpy.Exists("RESP"):
                #
                # if arcpy.Exists("RFCA"):
                #
                # if arcpy.Exists("RFCL"):
                #
                # if arcpy.Exists("RFCP"):
                #
                # if arcpy.Exists("RFZL"):
                #
                # if arcpy.Exists("RZJN"):
                #
                # if arcpy.Exists("HFCA"):
                #
                # if arcpy.Exists("HFCL"):
                #
                # if arcpy.Exists("HFCP"):
                #
                # if arcpy.Exists("HFZL"):
                #
                # if arcpy.Exists("HYDA"):
                #
                # if arcpy.Exists("HYDL"):
                #
                # if arcpy.Exists("HYDP"):
                #
                # if arcpy.Exists("HZJN"):
                #
                # if arcpy.Exists("VEGA"):
                #
                # if arcpy.Exists("VEGL"):
                #
                # if arcpy.Exists("VEGP"):
                #
                # if arcpy.Exists("VFZL"):
                #
                # if arcpy.Exists("VZJN"):
                #
                # if arcpy.Exists("ZFZA"):
                #
                # if arcpy.Exists("ZZJN"):
                #
                # if arcpy.Exists("TFCA_Add"):

                print u"处理完成"
if __name__ == '__main__':
      FCAlterAliasname(input_data,Output)
