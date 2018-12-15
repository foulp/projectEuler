# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 16:05:54 2016

@author: timothee.boulet
"""

def next_fraction(alpha,a,b):
    return [alpha*a+b,a]

seq=[2,1,2,1]
for k in xrange(2,34):
    seq.extend([1,2*k,1])

limit=99
e=[seq[limit],1]
for i in xrange(limit-1,-1,-1):
    e=next_fraction(seq[i],e[0],e[1])

print(sum([int(numb) for numb in str(e[0])]))



