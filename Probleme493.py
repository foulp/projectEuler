import numpy as np
  
p = np.zeros((8,21))
p[0,0] = 1
for N in xrange(1,21):
   for k in xrange(1,8):
      alpha = 10.*k - (N-1)
      beta = 70. - 10*(k-1)
      p[k,N] = alpha*p[k,N-1] + beta*p[k-1,N-1]
 
esp = 0
for k in xrange(8):
   esp += k * p[k,20]
print esp / sum(p[:,20])