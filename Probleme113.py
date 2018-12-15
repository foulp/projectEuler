"""Probleme 113""" #12951 for n<10**6 and 277032 for n<10**10
 
#sum([1 for i in xrange(1,10)]) + sum([1 for i in xrange(1,10)]) - 9
#
#sum([1 for i in xrange(1,10) for j in xrange(i,10)]) + sum([1 for i in xrange(1,10) for j in xrange(i+1) ]) - 9
#
#sum([1 for i in xrange(1,10) for j in xrange(i,10) for k in xrange(j,10)]) + sum([1 for i in xrange(1,10) for j in xrange(i+1) for k in xrange(j+1)]) - 9
#
#sum([1 for i in xrange(1,10) for j in xrange(i,10) for k in xrange(j,10) for l in xrange(k,10)]) + sum([1 for i in xrange(1,10) for j in xrange(i+1) for k in xrange(j+1) for l in xrange(k+1)]) - 9
#
#sum([1 for i in xrange(1,10) for j in xrange(i,10) for k in xrange(j,10) for l in xrange(k,10) for m in xrange(l,10)]) + sum([1 for i in xrange(1,10) for j in xrange(i+1) for k in xrange(j+1) for l in xrange(k+1) for m in xrange(l+1)]) - 9
#
#sum([1 for i in xrange(1,10) for j in xrange(i,10) for k in xrange(j,10) for l in xrange(k,10) for m in xrange(l,10) for n in xrange(m,10)]) + sum([1 for i in xrange(1,10) for j in xrange(i+1) for k in xrange(j+1) for l in xrange(k+1) for m in xrange(l+1) for n in xrange(m+1)]) - 9
#
#sum([1 for i in xrange(1,10) for j in xrange(i,10) for k in xrange(j,10) for l in xrange(k,10) for m in xrange(l,10) for n in xrange(m,10) for o in xrange(n,10)]) + sum([1 for i in xrange(1,10) for j in xrange(i+1) for k in xrange(j+1) for l in xrange(k+1) for m in xrange(l+1) for n in xrange(m+1) for o in xrange(n+1)]) - 9
#
#sum([1 for i in xrange(1,10) for j in xrange(i,10) for k in xrange(j,10) for l in xrange(k,10) for m in xrange(l,10) for n in xrange(m,10) for o in xrange(n,10) for p in xrange(o,10)]) + sum([1 for i in xrange(1,10) for j in xrange(i+1) for k in xrange(j+1) for l in xrange(k+1) for m in xrange(l+1) for n in xrange(m+1) for o in xrange(n+1) for p in xrange(o+1)]) - 9
#
#sum([1 for i in xrange(1,10) for j in xrange(i,10) for k in xrange(j,10) for l in xrange(k,10) for m in xrange(l,10) for n in xrange(m,10) for o in xrange(n,10) for p in xrange(o,10) for q in xrange(p,10)]) + sum([1 for i in xrange(1,10) for j in xrange(i+1) for k in xrange(j+1) for l in xrange(k+1) for m in xrange(l+1) for n in xrange(m+1) for o in xrange(n+1) for p in xrange(o+1) for q in xrange(p+1)]) - 9
#
#sum([1 for i in xrange(1,10) for j in xrange(i,10) for k in xrange(j,10) for l in xrange(k,10) for m in xrange(l,10) for n in xrange(m,10) for o in xrange(n,10) for p in xrange(o,10) for q in xrange(p,10) for r in xrange(q,10)]) + sum([1 for i in xrange(1,10) for j in xrange(i+1) for k in xrange(j+1) for l in xrange(k+1) for m in xrange(l+1) for n in xrange(m+1) for o in xrange(n+1) for p in xrange(o+1) for q in xrange(p+1) for r in xrange(q+1)]) - 9
 
import numpy as np
 
def compte(n):
total = 0
for m in xrange(n,0,-1):
for i in xrange(1,10):
sub1 = 1
sub2 = (-1)**(m-1)
for k in xrange(1,m):
sub1 *= (i+k) / float(k)
sub2 *= (i-(9+k)) / float(k)
total += sub1 + sub2
return total - 9*n
 
round(compte(100))