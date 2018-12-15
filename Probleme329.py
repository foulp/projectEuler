import numpy as np
from fractions import Fraction

NB_SQUARES = 500
SEQUENCE = 'PPPPNNPPPNPPNPN'

def next_step(i):
	if i==500:
		return 499
	if i==1:
		return 2
	return [i-1, i+1][random()<0.5]

def croak(i, c):
	if i in primes:
		return Fraction([1, 2][c=='P'], 3)
	return Fraction([1, 2][c=='N'], 3)

def primesfrom2to(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

primes = primesfrom2to(500)
current = {i: croak(i, SEQUENCE[0]) / NB_SQUARES for i in xrange(1,NB_SQUARES+1)}

for c in SEQUENCE[1:]:
	temp = {1: current[2] * croak(1, c) / 2}
	temp[2] = (current[1] + current[3] / 2) * croak(2,c)
	for square in xrange(3, NB_SQUARES-1):
		temp[square] = (current[square-1] + current[square+1]) * croak(square, c) / 2

	temp[499] = (current[500] + current[498] / 2) * croak(499,c)
	temp[500] = current[499] * croak(500,c) / 2

	current = dict(temp)

print sum(current.values())