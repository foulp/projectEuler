# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 22:13:25 2017

@author: SansAccent
"""
n = 50

scores2 = {0:0, 1:0, 2:1}
for i in xrange(3,n+1):
    scores2[i] = scores2[i-1] + scores2[i-2] + 1

scores3 = {0:0, 1:0, 2:0, 3:1}
for i in xrange(4,n+1):
    scores3[i] = scores3[i-1] + scores3[i-3] + 1

scores4 = {0:0, 1:0, 2:0, 3:0, 4:1}
for i in xrange(5,n+1):
    scores4[i] = scores4[i-1] + scores4[i-4] + 1

print scores2[n] + scores3[n] + scores4[n]