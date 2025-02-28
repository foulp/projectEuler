from numpy.polynomial import Polynomial
import numpy as np

s = []
N = 12
for b in range(1, 10**(N//2)):
    if b % 10**7 == 0:
        print(b)
    l = 10 ** (1 + int(np.log10(b)))
    p = Polynomial([b*(b-1), 2*b - l, 1])
    roots = p.roots()
    roots_ = [(int(a), b, int(a*l+b)) for a in roots if type(a) == np.float64 and int(a) == a and a > 0]
    s.extend(roots_)

print(s)
print(sum(c for a, b, c in s))
