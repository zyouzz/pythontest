#!/usr/bin/env python
#-*-coding:utf-8 -*-
__author__ = 'jiang'



url = "%E4%B8%AD%E6%96%87"
url1=url.replace('%', '')
print(url1)
url2=bytes.fromhex(url1)
print(url2.decode('utf-8'))




# print(urllib.unquote(url).decode("utf-8"))