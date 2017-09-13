#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import  arcpy
import xlsxwriter

InputFeature = arcpy.GetParameterAsText(0)
Outputxlsx = arcpy.GetParameterAsText(1)
xlsxfile = xlsxwriter.Workbook(Outputxlsx)
worksheet = xlsxfile.add_worksheet()
fields=arcpy.ListFields(InputFeature)
for field, num in zip(fields, range(len(fields))):
    worksheet.write(0, num, field.name)
i=1
with arcpy.da.SearchCursor(InputFeature,['*']) as cursor:
    for row in cursor:
        print list(row)
        for rr in list(row):
            print type(rr)
        for ii,rr in zip(range(len(list(fields))),list(row)):
            if ii==len(list(fields))-1:
                worksheet.write(i, ii, rr.__str__())
            else:
                worksheet.write(i, ii, rr)
        i+=1
xlsxfile.close()
