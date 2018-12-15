"""Problem 173"""

limit = 10**6
N_MAX = limit/4 + 1
r = 0

def tiles(n,k):
	return 4*(k+1)*(n-k-1)

for n in xrange(3,N_MAX+1):
	for k in xrange((n-3)/2 + 1):
		if tiles(n,k)<=limit: 
			r += 1
		else: 
			break

print r