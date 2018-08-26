# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 19:13:22 2018

@author: shurastogi
"""

import numpy as np

def matrix(vec,dimes,increasing):
    list_array=[]
    for y in range(dimes):
        list_ex=[x**y for x in vec]
        list_array.append(list_ex)
    if(increasing):
        return np.array(list_array).transpose()
    else:
        list_array=list_array[::-1]
        return np.array(list_array).transpose()
    
print(matrix([1,2,3,5],3,True))
print(matrix([1,2,3,5],3,False))