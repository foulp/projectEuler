import numpy as np

MAX_SUM = 9

N = 20

count = np.zeros((10,10,N))

def get_count(d1, d2, remain):
	if remain==0:
		return 1
	
	if count[d1,d2,remain]==0:
		for i in xrange(MAX_SUM-(d1+d2)+1):	
			count[d1,d2,remain] += get_count(d2, i, remain-1)
	return count[d1,d2,remain]

 print int(sum([get_count(0,i,N-1) for i in xrange(1,10)]))