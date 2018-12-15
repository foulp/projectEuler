# Indexing cards from 0 to size-1
# Trying to find how many moves to put card 1 back to its spot
# U_(n+1) = (2 * U_n) % (size-1)
# U_n = 2**n % (size-1)
# => 2**60 % (size-1) = 1 and  for all N<60: 2**N % (size-1) > 1

# The value s(n) hence satisfies the relation 2**s(n) % (n-1) = 1 ⟺ (n−1) divides 2**s(n) − 1

from operator import mul
import itertools
from itertools import combinations, chain

def powerset(iterable):
	s = list(iterable)
	return chain.from_iterable(combinations(s, r) for r in xrange(len(s)+1))

def prime_factors(n):
	for i in itertools.chain([2], itertools.count(3, 2)):
		if n <= 1:
			break
		while n % i == 0:
			n //= i
			yield i

def s(n):
 	if n==2:
 		return -1
 	curr, cnt = 2, 1
 	while curr!=1:
 		curr = (2*curr)%(n-1)
 		cnt+=1
 	return cnt

def s_inverse(k):
 	factors = prime_factors(2**k-1)
 	divisors = set([reduce(mul, subset, 1) for subset in powerset(factors)])
 	return [d+1 for d in divisors if s(d+1)==k ]

def S(k):
 	return sum(s_inverse(k))

print S(60)