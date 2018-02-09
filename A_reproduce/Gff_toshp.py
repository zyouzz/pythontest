#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import xlrd
import shapefile
import glob

def changeXls2shp(file):
    xls = xlrd.open_workbook(file)
    sheet = xls.sheet_by_index(0)


    w = shapefile.Writer(shapefile.POINT)

    for i in range (sheet.ncols):

        w.field(str(sheet.cell(0,i).value), "C", 40)
    for i in range(1,sheet.nrows):
        values = []
        for j in range(sheet.ncols):
            values.append(sheet.cell(i,j).value)
            print j
        w.record(*values)
        w.point(float(values[-2]),float(values[-1]))

    w.save(file)
def Read_file(workdir):
    list_dir = glob.glob(workdir)
    for i in list_dir:
        changeXls2shp(i)

if __name__ == '__main__':
    workdir='C:/Users/Esri/Desktop/GFF_Data/NYC_MUSEUMS_GEO1.xls'

    Read_file(workdir)