# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 23:49:45 2017

@author: SansAccent
"""

n = 50

scores = {0:1, 1:1, 2:2, 3:4}

for i in xrange(4,n+1):
    scores[i] = scores[i-1] + scores[i-2]+ scores[i-3]+ scores[i-4]

print scores[n]