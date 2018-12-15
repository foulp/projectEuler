# Pick's Theorem
# Aire = internal_edges + boundary_edges / 2 - 1
N = 100

from fractions import gcd
from itertools import product
import numpy as np

squared = np.zeros(2*N*N)
for i in xrange(int((2*N*N)**0.5)+1):
	squared[i*i] = 1

pointsEdge = np.zeros((N+1, N+1))
for a, b in product(xrange(1, N+1), repeat=2):
	pointsEdge[a,b] = pointsEdge[b,a] = gcd(a,b)

compte = 0
#for a, b, c, d in product(xrange(1, N+1), repeat=4):
for a in xrange(1, N+1):
	for b in xrange(1, a+1):
		for c in xrange(1, a+1):
			for d in xrange(1, b+1):
				internal_edges = ((a+c)*(b+d) - pointsEdge[a,b] - pointsEdge[b,c] - pointsEdge[c,d] - pointsEdge[d,a]) / 2 + 1
				if squared[int(internal_edges)]:
					add = 1
					if a!=b: add *= 2
					if a!=c: add *= 2
					if b!=d: add *= 2 
					compte += add

print compte