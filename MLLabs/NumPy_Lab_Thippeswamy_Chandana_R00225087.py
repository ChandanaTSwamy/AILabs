# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:07:29 2022

@author: Admin
"""

import numpy as ny
import pandas as pd

bike = pd.read_csv (r'F:\MTU\PythonScripts\AILabs\MLLabs\NumPy_Datasets\bike.csv')
#print (bike)

cork = ny.genfromtxt(fname='F:/MTU/PythonScripts/AILabs/MLLabs/NumPy_Datasets/CorkRainfall.txt')
print ('Printing Cork Data')
#print (cork)

#Find maximum ‘Most Rainfall in a Day’ value for the Cork data
arr1 = cork[:,3]
cork_max = ny.max(arr1)
print ('Maximum rainfall:', cork_max)

#Find average ‘Most Rainfall in a Day’ value for the Cork data
cork_avg = ny.average(cork[:,3])
print ('Average rainfall:', cork_avg)

#dublin = ny.genfromtxt(fname='F:/MTU/PythonScripts/AILabs/MLLabs/NumPy_Datasets/DublinRainfall.txt')
#print ('Printing Dublin Data')
#print (dublin)