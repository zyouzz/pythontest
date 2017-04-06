#-*-coding:utf-8 -*-
__author__ = 'kikita'

import struct

dbf = r'C:\Users\Esri\Desktop\diqu.dbf'
dat = open(dbf, 'rb').read(30)[29:]
id = struct.unpack('B', dat)[0]

print(id, hex(id))