# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 13:34:43 2017

@author: SansAccent
"""
import numpy as np

max_score = 36
colinDices, peteDices = 6, 9

Colin = np.zeros((max_score+1,colinDices+1))
Colin[0,0] = 1
for n in xrange(1,colinDices+1):
    for k in xrange(1,max_score+1):
        Colin[k,n] += sum([Colin[k-j,n-1] for j in xrange(1,7) if k-j>=0])
Colin = Colin/6**6
       
Pete = np.zeros((max_score+1,peteDices+1))
Pete[0,0] = 1
for n in xrange(1,peteDices+1):
    for k in xrange(1,max_score+1):
        Pete[k,n] += sum([Pete[k-j,n-1] for j in xrange(1,5) if k-j>=0])
Pete = Pete/4**9

total = 0
for k in xrange(4,37):
    total+=Colin[k,6]*sum([Pete[j,9] for j in xrange(k+1,max_score+1)])

print total