# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 15:42:12 2016

@author: timothee.boulet
"""

grid = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

best=75
choice = [0,1]

def path(seq):
    somme=75
    col=0
    for i, suivant in enumerate(seq) :
        col=col+suivant
        somme=somme+grid[i+1][col]
    return somme
    
for a in choice:
    for b in choice:
        for c in choice:
            for d in choice:
                for e in choice:
                    for f in choice:
                        for g in choice:
                            for h in choice:
                                for i in choice:
                                    for j in choice:
                                        for k in choice:
                                            for l in choice:
                                                for m in choice:
                                                    for n in choice:
                                                        best=max(best, path([a,b,c,d,e,f,g,h,i,j,k,l,m,n]))
print(best)
    
    