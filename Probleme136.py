"""Probleme 136"""
def primesList(n):
   primes = [True]*(n/2)
   for i in xrange(3,int(n**0.5)+1,2):
      if primes[i/2]:
         primes[i*i/2::i] = [False]*((n-i*i-1)/(2*i)+1)
   
   return [2]+[2*j+1 for j in xrange(1,n/2) if primes[j]]
 
limit = 50 * 10**6
primes = primesList(limit)
primes.remove(2)
primes.insert(0,1)
total = 0
for p in primes:
   if p%4==3: total+=1
   if 16*p<limit: total+=2
   elif 4*p<limit: total+=1
print total