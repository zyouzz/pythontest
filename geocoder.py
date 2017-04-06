#!/usr/bin/env python
#-*-coding:utf-8 -*-
__author__ = 'jiang'
import geocoder
g1 = geocoder.arcgis(u'Beijing')
print(g1.json)