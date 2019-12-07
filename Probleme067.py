# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 16:36:03 2016

@author: timothee.boulet
"""

text_file = open('Probleme67_triangle.txt', "r")
lines = text_file.read().split('\n')
text_file.close()

lines=lines[:-1]
lines=[[int(numb) for numb in line.split(' ')] for line in lines]

values=[[59]]
for i, line in enumerate(lines[1:]):
    temp=[]
    for j,numb in enumerate(line):
        if j==0:
            temp.append(numb+values[i][j])
        elif j==len(line)-1:
            temp.append(numb+values[i][j-1])
        else:
            temp.append(numb+max(values[i][j-1], values[i][j]))
    values.append(temp)

print(max(values[-1]))
