# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 11:54:30 2016

@author: timothee.boulet
"""
import numpy as np

f=open("C:\\Users\\timothee.boulet\\Desktop\\ProjectEuler\\Probleme81_matrix.txt",'r')
matrix=f.read().split('\n')[:-1]
f.close()

for i,line in enumerate(matrix) :
    matrix[i]=[int(numb) for numb in line.split(',')]


m=len(matrix)
values=np.zeros((m,m))
values[0,0]=matrix[0][0]
for j in range(1,m):
    values[0,j]=matrix[0][j]+values[0, j-1]
    values[j,0]=matrix[j][0]+values[j-1, 0]
for i in range(1,m):
    for j in range(1,m):
        values[i,j]=matrix[i][j]+min(values[i-1,j], values[i,j-1])

print(int(values[m-1,m-1]))
