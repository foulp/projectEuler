"""Probleme 146"""
from time import time
 
def MillerRabin_Prime(n):
   d = n-1
   s = 0
   while d%2==0:
      s+=1
      d/=2
   if n<2047:
      if pow(2,d,n)!=1 and all(pow(2,d*2**r,n)!=n-1 for r in xrange(s)):
         return False
   elif n<1373653:
      if any(pow(a%n,d,n)!=1 and all(pow(a%n,d*2**r,n)!=n-1 for r in xrange(s)) for a in [2,3]):
         return False
   elif n<9080191:
      if any(pow(a%n,d,n)!=1 and all(pow(a%n,d*2**r,n)!=n-1 for r in xrange(s)) for a in [31,73]):
         return False
   elif n<25326001:
      if any(pow(a%n,d,n)!=1 and all(pow(a%n,d*2**r,n)!=n-1 for r in xrange(s)) for a in [2,3,5]):
         return False
   elif n<3215031751:
      if any(pow(a%n,d,n)!=1 and all(pow(a%n,d*2**r,n)!=n-1 for r in xrange(s)) for a in [2,3,5,7]):
         return False
   elif n<4759123141:
      if any(pow(a%n,d,n)!=1 and all(pow(a%n,d*2**r,n)!=n-1 for r in xrange(s)) for a in [2,7,61]):
         return False
   elif n<1122004669633:
      if any(pow(a%n,d,n)!=1 and all(pow(a%n,d*2**r,n)!=n-1 for r in xrange(s)) for a in [2,13,23,1662803]):
         return False
   elif n<2152302898747:
      if any(pow(a%n,d,n)!=1 and all(pow(a%n,d*2**r,n)!=n-1 for r in xrange(s)) for a in [2,3,5,7,11]):
         return False
   elif n<3474749660383:
      if any(pow(a%n,d,n)!=1 and all(pow(a%n,d*2**r,n)!=n-1 for r in xrange(s)) for a in [2,3,5,7,11,13]):
         return False
   elif n<341550071728321:
      if any(pow(a%n,d,n)!=1 and all(pow(a%n,d*2**r,n)!=n-1 for r in xrange(s)) for a in [2,3,5,7,11,13,17]):
         return False
   elif n<3825123056546413051:
      if any(pow(a%n,d,n)!=1 and all(pow(a%n,d*2**r,n)!=n-1 for r in xrange(s)) for a in [2,3,5,7,11,13,17,19,23]):
         return False
  
   return True
 
      
def mods(m):
   result = []
   for k in xrange(m):
      if all((k**2+j)%m!=0 for j in (1,3,7,9,13,27)):
         result.append(k)
   return result
  
primes = primesList(100)
Mods = [mods(p) for p in primes]
t=time()
limit = 15*10**7
total = 0
for j in xrange(0,limit,210):
   for n in [j+10,j+80,j+130,j+200]:
      if all(n%p in Mods[i] for i,p in enumerate(primes)):
         if all(MillerRabin_Prime(n**2+k) for k in [1,3,7,9,13,27]) and all(MillerRabin_Prime(n**2+k)==False for k in [19,21]):
            print "Found:",n, time()-t
            total+=n        
      
print total, time()-t