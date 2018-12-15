from time import time
import numpy as np

def modInverse(a, p):
	return pow(a, p-2, p)

def modFact(n, p):
	res = p-1
	for i in xrange(n+1, p):
		res = (res * modInverse(i,p)) % p
	return res

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

LIMIT = 10**8

"""t=time()
total = 0
for p in xrange(5, LIMIT, 2):
	if isPrime(p):
		total += 9*modFact(p-5,p) % p
print total, time()-t"""

t=time()
total = 0
for p in primesfrom2to(LIMIT)[2:]:
	total += 9*modFact(p-5,p) % p
print total, time()-t