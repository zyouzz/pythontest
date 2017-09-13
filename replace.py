#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
with open(r"C:\Users\Esri\Desktop\DrawingMillions_of_Features_in_ArcGIS_1100_Final.srt") as srt:
    files = open(r'C:\Users\Esri\Desktop\neww.srt', 'a+')
    for line in srt:
        if "-->" in line:
            line=line.replace('.',',')
        files.write(line)
    files.close()
