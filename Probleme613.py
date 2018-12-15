import math
from scipy.integrate import dblquad

a = 3.
b = 4.

f = lambda y, x: math.pi/2. + math.atan(x/(a-y)) + math.atan(y/(b-x))

result = dblquad(f, 0., b, lambda x: 0., lambda x: -a/b*x+a)[0]

print round(result / (2.*math.pi) / (a*b/2.), 10)