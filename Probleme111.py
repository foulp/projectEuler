from itertools import permutations, product
 
def isPrime(n):
   if n<=1:
      return False
   if n in [2,3,5,7]:
      return True
   if n%10 in [0,2,4,5,6,8]:
      return False
   for i in xrange(3, int(n**0.5)+1, 2):
      if n%i==0:
         return False
   return True
 
d=10
array = [[0]]*10
current = {k:0 for k in xrange(10)}
for i in range(10):
   k = 9
   while current[i]==0:
      for liste in product(xrange(10), repeat=d-k):
         for n in set(permutations([i]*k+list(liste))):
            numb = int(''.join([str(g) for g in n]))
            if len(str(numb))==d and isPrime(numb):
               array[i] = liste(set(array[i])) + [numb]
               current[i] = k
      print k
      k-=1
     
         
print sum([sum(set(val)) for val in array])