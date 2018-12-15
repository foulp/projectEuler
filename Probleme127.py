"""Probleme 127"""
from time import time
from fractions import gcd
import numpy as np

def radicals(n):
	result = {x:1 for x in xrange(1,n+1)}
	for i in xrange(2,n):
		if result[i]==1:
			k = 1
			while k*i<=n:
				result[k*i] *= i
				k += 1
	return result
 
n = 120000
rads = radicals(n)
t=time()
total = 0
for c in xrange(3,n):
	if c%1000==0:
		print c
	crad = rads[c]
	l = float(c) / crad
	if rads[c-1] < l:
		total += c
	m = c%2
	stop = (m==1)*6 + (m==0)*15
	if l<=stop:
		continue
	for a in xrange(3-m,c/2+1,2-m):
		arad = rads[a]
		if gcd(a,c)!=1 or stop>=l:
			continue
		test = arad * rads[c-a]
		if test < l:
			total += c
print time()-t,total