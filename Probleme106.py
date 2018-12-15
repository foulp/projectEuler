"""Probleme 106"""
from itertools import combinations
n = 12
el = list(xrange(1,n+1))
total = 0
for i in xrange(2,n/2+1):
   comb = list(combinations(el, i))
   for j, cj in enumerate(comb):
      for c in comb[j+1:]:
         if all(a not in c for a in cj):
            if all(c[k]<cj[k] for k in xrange(i)) or all(c[k]>cj[k] for k in xrange(i)):
               pass
            else:
               total+=1
print total
 