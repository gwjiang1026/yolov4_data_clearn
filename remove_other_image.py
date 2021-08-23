# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 13:57:52 2021

@author: GWJIANG
"""

import glob
import os

arr = os.listdir(r'C:\Users\GWJIANG\Desktop\GW\python code\yolov4\downloads\train_0720')
arr = sorted(arr)

after = []
remove = []


for i in range(len(arr)):

    str2 = arr[i].split('.')[0]
    if i == 0:
        pass
    
    if arr[i].split('.')[0] != arr[i-1].split('.')[0] and arr[i].split('.')[0] != arr[i+1].split('.')[0]:
        remove.append(arr[i])


print (remove)


for filename in os.listdir(r'C:\Users\GWJIANG\Desktop\GW\python code\yolov4\downloads\train_0720'):
    print(filename)
    if filename in remove:
        os.remove(r'C:\Users\GWJIANG\Desktop\GW\python code\yolov4\downloads\train_0720'+'\\'+ filename)