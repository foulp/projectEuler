# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 12:22:00 2016

@author: timothee.boulet
"""

element=[0,1,2,3,4,5,6,7,8,9]

from itertools import permutations

seq = list(permutations(element))
seq.sort()
print(seq[999999])
 
                                        