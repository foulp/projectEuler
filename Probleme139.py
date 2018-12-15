"""Probleme 139"""
from fractions import gcd
limit = 10**8
pmax = int((limit/2.)**0.5)
compte = 0
for p in xrange(2,pmax):
if p%100==0:print p
stop = min(p, int(5.*10**7/p - p) + 1)
for q in xrange(1+p%2,stop,2):
if gcd(p,q)==1:
a, b, c = p**2-q**2, 2*p*q, p**2+q**2
kmax = int(limit / float(a+b+c))
test = float(k*c) / abs(k*a-k*b)
if test==int(test):
compte+=kmax