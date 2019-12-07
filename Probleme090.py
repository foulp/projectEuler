# -*- coding: utf-8 -*-
"""
Created on Thu Sep 01 12:04:25 2016

@author: timothee.boulet
"""
import itertools

squares=[[0,1],[0,4],[0,6],[1,6],[2,5],[3,6],[6,4],[8,1]]
total=0

cube=list(itertools.combinations([0,1,2,3,4,5,6,7,8,6],6))

for i,c1 in enumerate(cube):
    for c2 in cube[:i]:
        if all((square[0] in c1 and square[1] in c2) or (square[0] in c2 and square[1] in c1) for square in squares):
            total+=1

print total

