from math import sqrt
from fractions import gcd
 
limit=10**12
somme = 0
for a in xrange(2,10**4):
   for b in xrange(1,a):
      if gcd(a,b)==1 and b*(a**3+b)<limit:
         c = 1
         test = c*b*(a**3*c+b)
         while test<limit:
            if int(sqrt(test))==sqrt(test):
               somme+=test
            c+=1
            test = c*b*(a**3*c+b)
print somme