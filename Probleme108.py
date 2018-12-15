#1/x+1/y=1/n <=> x = yn/(y-n) <=> x = (n+k)*n/k, 1<=k<=n <=> x = n + n**2/k, 1<=k<=n, <=> x entier naturel>0 ssi k divise n**2, 1<=k<=n
# <=> (NbDiviseurs de n**2+1)/2 = NbSolutions
 
# NbDiviseurs de n**2 = prod(2*ai+1), où n=prod(pi**ai)
# Il faut prod(2*ai+1)>2*1000
# Or 3**7=2187 donc Nmax = 2*3*5*7*11*13*17
 
n=2*3*5*7*11*13*17
for a1 in xrange(0,6):
   for a2 in xrange(0,a1+1):
      for a3 in xrange(0,a2+1):
         for a4 in xrange(0,a3+1):
            for a5 in xrange(0,a4+1):
               for a6 in xrange(0,a5+1):
                  for a7 in xrange(0,a6+1):
                     if (2*a1+1)*(2*a2+1)*(2*a3+1)*(2*a4+1)*(2*a5+1)*(2*a6+1)*(2*a7+1)>2000:
                        n = min(n,2**a1*3**a2*5**a3*7**a4*11**a5*13**a6*17**a7)
 
print n