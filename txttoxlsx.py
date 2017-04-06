#!/usr/bin/env python
# -*-coding:utf-8 -*-
# __author__ = 'jiang'
import xlsxwriter


def txttoxlsx(txtpath):
    exc = xlsxwriter.Workbook(
        'C://Users//Esri//Desktop//statistics//' + txtpath.split('//')[-1].split('.')[0] + '.xlsx')
    worksheet = exc.add_worksheet()
    openf = open(txtpath, 'r', encoding='utf-8')
    opentxt = openf.read().split('\n')
    colnums = len(opentxt[0].split(','))
    print(colnums)
    maxwidth = 0
    i=0
    for colnum in range(0, colnums):
        if '' != opentxt[len(opentxt) - 1]:
            length = len(opentxt)

        else:
            i+=1
            length = len(opentxt) - i
        for linenums in range(0, length):
            print(len(opentxt))
            wid = len(opentxt[linenums].split(',')[colnum])
            if wid >= maxwidth:
                maxwidth = wid
        worksheet.set_column(colnum, colnum, width=maxwidth)
        for linenum in range(0, length):
            worksheet.write(linenum, colnum, opentxt[linenum].split(',')[colnum])
    exc.close()
    '''文本信息'''
    print('该文本有%d行为空' % i)

txttoxlsx('C://Users//Esri//Desktop//statistics//duplicatebeta.txt')
