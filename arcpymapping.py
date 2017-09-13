#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
# coding: utf-8
"""
Tool Name:     Global Moran's I
Source Name:   GlobalI.py
Version:       ArcGIS 10.1
Author:        Environmental Systems Research Institute Inc.
Description:   Computes Global Moran's I statistic
"""

################### Imports ########################
import sys as SYS
import os as OS
import glob as GLOB
import numpy as NUM
import xml.etree.ElementTree as ET
import arcgisscripting as ARC
import arcpy
import ErrorUtils as ERROR
import SSUtilities as UTILS
import SSDataObject as SSDO
import Stats as STATS
import WeightsUtilities as WU
import gapy as GAPY
import SSReport as REPORT
import locale as LOCALE

LOCALE.setlocale(LOCALE.LC_ALL, '')


################### GUI Interface ###################



def mapping():
    mxd = arcpy.mapping.MapDocument(r"D:\协助各省\辽宁\2-1农产品产地土壤pH含量分布图.mxd")
    df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
    lyrs = arcpy.mapping.ListLayers(mxd)
    calyr = lyrs[0]
    salyr = lyrs[1]
    prlyr = lyrs[2]

    base = "D:\\2017.06.27全国数据\\"
    caDir = base + "全国省会拆分P"
    saDir = "D:\CZ201708\HgGD.gdb"
    prDir = base + "全国省界拆分P"

    for filepath in GLOB.glob(prDir + "\\*.shp"):
        filenameShp = filepath.split("\\")[3]
        filename = filenameShp.split(".")[0]
        print saDir + "\\" + filenameShp
        print filename
        if ((cmp(filename, "台湾省") == 0) or (cmp(filename, "澳门特别行政区") == 0) or (cmp(filename, "香港特别行政区") == 0)):
            continue

        calyr.replaceDataSource(caDir, "SHAPEFILE_WORKSPACE", filename)
        salyr.replaceDataSource(saDir, "FILEGDB_WORKSPACE", filename)
        prlyr.replaceDataSource(prDir, "SHAPEFILE_WORKSPACE", filename)

        # extentTest=blyr.getExtent().projectAs(df.extent.spatialReference)
        extent = prlyr.getExtent().projectAs(df.spatialReference)
        # extent=prlyr.getExtent()
        df.extent = arcpy.Extent(extent.XMin - 0.1 * extent.width, extent.YMin - 0.1 * extent.height,
                                 extent.XMax + 0.1 * extent.width, extent.YMax + 0.1 * extent.height)
        # df.spatialReference=extent.spatialReference

        sourceLayer = arcpy.mapping.Layer(r"D:\2017.06.27全国数据\出图\2-1农产品产地土壤pH含量分布图\湖北省.lyr")
        arcpy.mapping.UpdateLayer(df, salyr, sourceLayer, True)
        if salyr.symbologyType == "RASTER_CLASSIFIED":
            salyr.symbology.reclassify()
        arcpy.RefreshTOC()
        arcpy.RefreshActiveView()
        arcpy.mapping.ExportToJPEG(mxd, ("D:\\2017.06.27全国数据\\出图\\2-1农产品产地土壤pH含量分布图\\" + filename + ".jpg"),resolution=350)


if __name__ == "__main__":
    mapping()