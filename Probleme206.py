# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 23:18:38 2017

@author: SansAccent
"""

from time import time
"""
(k*100+30)**2 = 10000*k**2 + 6000*k + 900
(a+10)**2 = a**2 + 20*a + 100
"""
import re
t=time()
d = int(1020304050607080900**0.5)
d = d-d%100+30
rule = r'1\d2\d3\d4\d5\d6\d7\d8\d900'
while re.match(rule, str(d**2))==None:
    d+=40
    if re.match(rule, str(d**2))==None:
        d+=60
print d, d**2