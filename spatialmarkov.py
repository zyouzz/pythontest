#!/usr/bin/env python
# -*-coding:utf-8 -*-
# __author__ = 'jiang'
import pysal as ps
import numpy as np
f = ps.open(r"D:\Python 3.5\Lib\site-packages\pysal\examples\us_income\usjoin.csv")
pci = np.array([f.by_col[str(y)] for y in range(1929, 2010)])
pci = pci.transpose()
rpci = pci / (pci.mean(axis=0))
w = ps.open(r"D:\Python 3.5\Lib\site-packages\pysal\examples\us_income\states48.gal").read()
w.transform = 'r'
sm = ps.Spatial_Markov(rpci, w, fixed=True, k=5, variable_name='rpci')
for p in sm.P:
    print(p)
