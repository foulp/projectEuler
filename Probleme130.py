From math import log10
 
size = 10**5
primes = [1]*size
primes[0], primes[1] = 0, 0
for p,prime in enumerate(primes):
   if prime==1:
      k = 2
      while k*p<size:
         primes[k*p] = 0
         k += 1
noPrime = [j for j,val in enumerate(primes) if val==0 and j>1 and j%10 in [1,3,7,9]]
 
limit = 25
n, compte = noPrime[0], 0
compteur, somme = 0, 0
while compteur<limit:
   k = max(1,int(log10(n)))
   test = int('1'*k)%n
   while test!=0:
      test = (test*10+1)%n
      k += 1
   if (n-1)%k==0:
      print n,k
      compteur += 1
      somme += n
   compte+=1
   n=noPrime[compte]
print somme