LIMIT = 10**12

# For all n >= 3, n = 11 in base n-1 as n = 1*(n-1) + 1
# So we must find n such that: n = 111 in some base, or n = 1111, or n = 11111, ...

liste = set([1]) # 1 is a repunit in all bases 
i = 2
j = 3
current = sum([i**k for k in xrange(j)]) # We start with 1*2**2 + 1*2 + 1
while current < LIMIT:
	while current < LIMIT:
		liste.add(current)
		j += 1
		current = sum([i**k for k in xrange(j)])
	i += 1
	j = 3
	current = sum([i**k for k in xrange(j)])

print sum(liste)