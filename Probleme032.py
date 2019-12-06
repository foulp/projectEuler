# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 11:00:33 2016

@author: timothee.boulet
"""

import itertools

elements=list(range(1,10))

collections=itertools.permutations(elements)

final = []
for seq in collections:
    for prod in [1,2,3,4,5,6,7]:
        for equal in list(range(prod+1,9)):
            term1 = int(''.join([str(nb) for nb in seq[:prod]]))
            term2 = int(''.join([str(nb) for nb in seq[prod:equal]]))
            result = int(''.join([str(nb) for nb in seq[equal:]]))
            if result not in final and term1*term2==result:
                final.append(result)

print(sum(final))
