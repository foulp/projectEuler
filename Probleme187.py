n = 10**8
primes = primesList(n/2)
k=len(primes)-1
compteur = 0
for i,prime in enumerate(primes):
if prime>10**4:
break
while prime*primes[k]>=n:
k-=1
compteur += k+1-i
print compteur