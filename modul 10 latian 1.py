# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 20:36:55 2022

@author: fariz
"""
data= [87,56, 34, 23,89,15,2,200,28,31, 2]

def bubbleSort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1] :
                a[j], a[j+1] = a[j+1], a[j]
    return a

def cari_b(x,y,l=0):
    r=len(y)
    while l<=r:
        m=(l+r)//2
        if x==y[m]:
            return m
        elif x<y[m]:
            r=m-1
        else:
            l=m+1
    return-1

print(data)
cari=int(input('angka yg di cari: '))
urut=bubbleSort(data)
print(urut)
hasil=cari_b(cari,urut)
if hasil==-1:
    print('element tidak di temukan')
else:
    print(f'element di temukan di posisi ke {hasil+1}')