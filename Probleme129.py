"""Probleme 129"""

from math import log10
 
limit = 10**6
n, A, compte = 10**6-1, 1, -1

while A<=limit:
   n+=2*(1+(compte==1))
   compte = (compte+1)%4
   A = max(1,int(log10(n)))
   test = int(A*'1')%n
   while test!=0:
      test = (10*test+1)%n
      A+=1
      
print n