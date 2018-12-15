"""Problem 191"""

import numpy as np

N_DAYS = 30
count = np.zeros((2,4,N_DAYS+1))

def correct(dL, dA, remain):
	if remain==0:
      return 1

   if count[dL, dA, remain]==0:
      for v in 'OAL':
         if dL+(v=='L')<2 and (1+dA)*(v=='A')<3:
            count[dL,dA, remain] += correct(dL+(v=='L'), (1+dA)*(v=='A'), remain-1)
   return count[dL, dA, remain]

print int(correct(0,0,N_DAYS))