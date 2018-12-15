"""Probleme 144"""
import numpy as np
epsilon = 0.0000001
Xs = [(0,10.1), (1.4,-9.6)]
i = 0
while abs(Xs[-1][0])>0.01 or Xs[-1][1]<0:
   i+=1
   x, y = Xs[-1]
   a = (y - Xs[-2][1]) / float(x - Xs[-2][0])
  
   if x!=0 and y!=0:
      aN = -4.*x/y
      aNew = (aN*(a*aN+2) - a) /float(aN*(2*a-aN) + 1)
   else:
      aNew = -a
     
   b = y - aNew*x
  
   xNext = np.roots([4 + aNew**2, 2*aNew*b, b**2 - 100])
   x = xNext[abs(xNext-x)>epsilon][0]
   y = aNew*x + b
   Xs.append((x,y))
     
print "La réponse est :", i  