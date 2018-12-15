# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 18:39:57 2016

@author: Timothée Boulet
"""
somme=0
for a in range(100):
    for b in range(100):
        somme=max(somme,sum([int(i) for i in list(str(a**b))]))
print(somme)

"""
Answer : 972
"""