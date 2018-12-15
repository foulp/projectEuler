limit = 10**6
primes = [1]*limit
primes[0] = primes[1] = 0
for j,prime in enumerate(primes):
   if prime==1:
      k = 2*j
      while k<limit:
         primes[k] = 0
         k += j
primes = [j for j,prime in enumerate(primes) if prime==1]
 
         
stop = 0
while (stop+1)**3-stop**3<limit:
   stop+=1
         
total=0
for x in xrange(stop):
    if (x+1)**3-x**3 in primes:
        total+=1
 
print total