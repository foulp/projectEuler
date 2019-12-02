from time import time

t = time()
LIMIT = 10**8
kempner = [0]*(LIMIT+1)

for i in xrange(2, LIMIT+1):
	if i%(10**6) == 0:
		print i

	if kempner[i] == 0:  # i is prime
		power = 1
		prime = i
		p_met = 0
		m = 0
		while prime <= LIMIT:
			while p_met < power:
				m += i
				temp = int(m)
				while temp % i == 0:
					p_met +=1
					temp /= i

			# Update answer for all multiples of 'prime'
			for k in xrange(prime, LIMIT + 1, prime):
				kempner[k] = max(m, kempner[k])

			power += 1
			prime *= i

print sum(kempner) # 476001479068717
print 'Time needed : ', time() - t # 169.57