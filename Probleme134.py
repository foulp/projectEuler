from math import log10
 
def pgcd(a,b):
   if a==1 or b==1:
      return 1
   if a<b:
      a, b = b, a
   while a%b!=0:
      a, b = b, a%b
   return b
 
def euclide(a,b):
   r1, u1, v1, r2, u2, v2 = a, 1, 0, b, 0, 1
   while r2!=0:
      q = int(r1/r2)
      r1, u1, v1, r2, u2, v2 = r2, u2, v2, r1 - q *r2, u1 - q*u2, v1 - q*v2
   return r1,u1,v1
   
limit = int(1.1*10**6)
primes = [1]*limit
primes[0] = primes[1] = 0
for j,p in enumerate(primes):
   if p==1:
      a=2*j
      while a<limit:
         primes[a] = 0
         a+=j
primes = [j for j,p in enumerate(primes) if p==1][2:]
 
#x*10**d(p1)+p1 = 0 mod(p2) soit x*10**d(p1) = (p2-p1) mod(p2)
total = 0
for j,p in enumerate(primes[:-1]):
   if p>10**6:
      break
   A = 10**(int(log10(p))+1)
   B = primes[j+1]-p
   M = primes[j+1]
   _,c,_ = euclide(A,M)
     
   x = (c*B)%M
   total += x*A+p
  
print int(total)