#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 08:32:23 2017

@author: akankshya
"""
import numpy as np
import sys
import csv


#m=eval(raw_input('enter M:'))
#n=eval(raw_input('enter N:'))
m=8
n=8
p=100;
x_r= np.random.normal(0, np.sqrt(p/2), m*n)
x_i=np.random.normal(0, np.sqrt(p/2), m*n)
cdbk=np.transpose([x_r,x_i])
np.savetxt("noise.csv", cdbk, delimiter=",") 
with open('noise.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print ("hello")
