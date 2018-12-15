from itertools import permutations
from time import time
 
def primesList(n):
   primes = [True]*(n/2)
   for i in xrange(3,int(n**0.5)+1,2):
      if primes[i/2]:
         primes[i*i/2::i] = [False]*((n-i*i-1)/(2*i)+1)
   
   return [2]+[2*j+1 for j in xrange(1,n/2) if primes[j]]
t=time()
numberOfDigit = 9
limit = 10**(numberOfDigit-1)
primes = primesList(limit)
primes = [p for p in primes if all(str(p).count(str(d))<=1 for d in xrange(1,numberOfDigit+1))]
 
def nbSet(digits, primes):
   parite = {d:int(d)%2 for d in digits}
   b = parite.values().count(1)
   if b==0:
      return 0
     
   elif b==1:
      evens = {d for d,v in parite.iteritems() if v==0}
      odd = (digits-evens).pop()
      compte = sum([int(''.join(p)+odd) in primes for p in permutations(evens)])
      return compte
     
   else:
      compteur = 0
      for k in xrange(len(primes)):
         string = str(primes[k])
         if len(string)>len(digits):
            break
        
         if all(d in digits for d in string):
            digit = digits-set(list(string))
            if len(digit)>0:
               compteur += nbSet(digit, primes[k+1:])
            else:
               compteur+=1
 
      return compteur
     
print nbSet({str(d) for d in xrange(1,numberOfDigit+1)}, primes), time()-t
#%%
from math import sqrt
from itertools import combinations, permutations
from time import time
start = time()
 
def primesList(n):
   primes = [True]*(n/2)
   for i in xrange(3,int(n**0.5)+1,2):
      if primes[i/2]:
         primes[i*i/2::i] = [False]*((n-i*i-1)/(2*i)+1)
   
   return [2]+[2*j+1 for j in xrange(1,n/2) if primes[j]]
 
numberOfDigit = 9
limit = int(sqrt(10**((numberOfDigit-1))))+1
primes = primesList(limit)
 
def isPrime(n):
    if n==1:
        return False
 
    upperlimit = int(n**0.5)
 
    for p in primes:
        if p>upperlimit:
            break
        if 0==n%p:
           return False
    return True
 
primesetsdict = {tuple() : 1}
 
def primesets(numsleft):
    if tuple(numsleft) in primesetsdict:
        return primesetsdict[tuple(numsleft)]
 
    answer = 0
    forcednum = numsleft[0]
    possibleextras = len(numsleft)-1
 
    for numextras in range(possibleextras+1):
        for e in combinations(numsleft[1:], numextras):
            extras = list(e)
 
            newnumsleft = [ix for ix in numsleft[1:] if ix not in extras]
 
            for p in permutations(extras + [forcednum]):
                if isPrime(sum([d*10**i for i,d in enumerate(list(p))])):
                    answer += primesets(newnumsleft)
   
    primesetsdict[tuple(numsleft)] = answer
    return answer
 
print "Answer: ", primesets([1,2,3,4,5,6,7,8,9])
print "Time: ", time() - start