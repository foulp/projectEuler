# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 22:58:32 2017

@author: SansAccent
"""

import numpy as np
n, m = 30, 60
probas = np.zeros((20000,200))
probas[0,0] = 1

for k in xrange(1,200):
    for t in xrange(20000):
        probas[t,k] += 1./(m-n+1) * sum([probas[t-5-j, k-1] for j in xrange(n,m+1) if t-5-j>=0])

esp = 0
for t in xrange(1,20000):
    esp += t*sum([probas[t,k]*sum(probas[t+1:,k-1]) for k in xrange(200)])