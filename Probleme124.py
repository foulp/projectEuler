def isPrime(n):
   if n<=1:
      return False
   if n in [2,3,5,7]:
      return True
   if n%10 in [0,2,4,5,6,8]:
      return False
   for i in range(3,int(n**0.5)+1,2):
      if n%i==0:
         return False
   return True
  
factor=[[1]]*(10**5+1)
for i in range(2,10**5+1):
   if isPrime(i):
      k=1
      while k*i<=10**5:
         factor[k*i]=factor[k*i]+[i]
         k+=1
 
import numpy as np
rad = [[np.prod(np.array(factor[n])),n] for n in range(1,10**5+1)]
rad.sort()
rad[9999][1]
