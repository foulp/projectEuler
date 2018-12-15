import numpy as np

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k = 3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

N = 100000000

temp = primesfrom2to(N+2)
primes = np.zeros(N+2)
primes[temp] = 1
print 'There are %d primes to %d' % (np.sum(primes), N)

def check(cand, primes):
	for d in xrange(2, int(cand**0.5) + 1):
		if cand % d == 0 and not primes[cand//d+d]:
			return False
	return True

s = 1 + 2

for cand in xrange(6, N, 4):
	if primes[cand+1] and check(cand, primes):
		s += cand

print s