#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
with open(r'C:\Users\Esri\Desktop\ss2.txt') as txt:
    lines = txt.readlines()
    i=1
    for line in lines:
        if len(line.split(';'))==2:
            xx="A "+line.split(';')[0]+'<br>'+"B "+line.split(';')[1]
        elif len(line.split(';'))==3:
            xx = "A " + line.split(';')[0] + '<br>' + "B " + line.split(';')[1] + '<br>' + "C " + line.split(';')[2]
        elif len(line.split(';'))==4:
            xx="A "+line.split(';')[0]+'<br>'+"B "+line.split(';')[1]+'<br>'+"C "+line.split(';')[2]+'<br>'+"D "+line.split(';')[3]
        elif len(line.split(';')) == 5:
            xx = "A " + line.split(';')[0] + '<br>' + "B " + line.split(';')[1] + '<br>' + "C " + line.split(';')[2] + '<br>' + "D " + line.split(';')[3] + '<br>' + "E " + line.split(';')[4]
        elif len(line.split(';')) == 6:
            xx = "A " + line.split(';')[0] + '<br>' + "B " + line.split(';')[1] + '<br>' + "C " + line.split(';')[2] + '<br>' + "D " + line.split(';')[3]+ '<br>' + "E " + line.split(';')[4]+ '<br>' + "F " + line.split(';')[5]
        files = open(r'C:\Users\Esri\Desktop\tx22.txt', 'a+')
        files.write(xx)
