# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 05:13:52 2022

@author: fariz
"""

def bubbleSort(a,b=0):
    n = len(a)
    if b<n:
        for j in range(0, n-b-1):
            if a[j] > a[j+1] :
                a[j], a[j+1] = a[j+1], a[j]
                b+=1
                bubbleSort(a,b)
    return a

data= [87,56, 34, 23,89,15,2,200,28,31, 2]
print(data)
urut=bubbleSort(data)
print(urut)