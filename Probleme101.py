from numpy.polynomial import polynomial as P
from numpy.polynomial.polynomial import polyval
 
def suite(n):
   total = 0
   for i in range(11):
      total+=pow(-n,i)
   return total
 
def OP(k,n):
   #Optimum polynom of degree k
   #Nth value of the suite base on this optimum polynome
   x = list(range(1,k+1))
   y = [suite(xi) for xi in x]
   c = P.polyfit(x,y, k-1)
  
   for i,v in enumerate(c):
      c[i]=round(v)
     
   return polyval(n,c)
 
def FIT(k):
   return OP(k,k+1)
 
somme=0
for i in range(1,11):
   somme+=FIT(i)