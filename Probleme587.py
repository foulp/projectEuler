from math import acos, sin, pi
limit = 0.001
k = 1
n = 0
while k>=limit:
   n+=1
   alpha = (2.*n*(1+n)-(2*n)**1.5) / (2.*(1+n**2))
   k = alpha**2/(2.*n) + 1-alpha - 1./2*(pi/2.-acos(1-alpha)) - 1/4.*sin(2*acos(1-alpha))
   k/=float((1-pi/4.))
  
print n,k