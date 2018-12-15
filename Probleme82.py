# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 11:54:30 2016

@author: timothee.boulet
"""
import numpy as np

f=open("C:\\Users\\timothee.boulet\\Desktop\\ProjectEuler\\Probleme82_matrix.txt",'r')
matrix=f.read().split('\n')[:-1]
f.close()

for i,line in enumerate(matrix) :
    matrix[i]=[int(numb) for numb in line.split(',')]

#matrix=[[131,673,234,103,18],
#        [201,96,342,965,150],
#        [630,803,745,422,111],
#        [537,699,497,121,956],
#        [805,732,524,37,331]]


m=len(matrix)
values=np.zeros((m,m))

for i in range(m):
    values[i,0]=matrix[i][0]

for j in range(1,m):
    for i in range(m):
        temp=[]
        for l in range(m):
            if l<i:
                temp.append(values[l,j-1]+sum([matrix[k][j] for k in range(l,i+1)]) )
            if i==l:            
                temp.append(matrix[i][j]+values[i,j-1])
            if l>i:
                temp.append(values[l,j-1]+sum([matrix[k][j] for k in range(i,l+1)]) )
        values[i,j]=min(temp)
    
print(int(min(values[:,-1])))