# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 09:31:19 2021

@author: GWJIANG
"""
import os

path = r'C:\Users\GWJIANG\Desktop\GW\python code\yolov4\downloads\down'
i = 0
for filename in os.listdir(path):
    print(filename)
    os.rename(os.path.join(path,filename), os.path.join(path,'down'+str(i)+'.jpg'))
    i = i +1