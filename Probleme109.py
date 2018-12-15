# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 18:31:14 2017

@author: SansAccent
"""
import numpy as np

simples = np.array(list(xrange(1,21)) + [25])
doubles = 2*simples
triples = np.delete(3*simples, -1)

n = 99
scores = np.zeros((n+1,4))
scores[0,0] = 1
scores[doubles[:n/2],1] = 1

for j in xrange(2,4):
    for i in xrange(2,n+1):
        scores[i,j] = np.sum(scores[[i-val for val in simples if i>val], j-1])
        scores[i,j] += np.sum(scores[[i-val for val in doubles if i>val], j-1])
        scores[i,j] += np.sum(scores[[i-val for val in triples if i>val], j-1])

for i in xrange(4,n+1):
    if i%2==0:
        val = (i-np.where(scores[:i,1]==1)[0]) / 2
        total = len(np.intersect1d(val, simples))
        total += len(np.intersect1d(val, doubles))
        total += len(np.intersect1d(val, triples))
        scores[i,3] = (scores[i,3] + total) / 2
    else:
        scores[i,3] /= 2
        
print int(np.sum(scores)-1)

