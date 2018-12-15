"""Probleme 135"""
def divisorsList(n):
	divisors = {x:[(x,1)] for x in xrange(2,n+1)}
	for k in xrange(2,n/2+1):
		i = 2
		while i<k and k*i<=n:
			divisors[k*i] = divisors[k*i] + [(k,i)]
			i+=1
	for k in xrange(2,int(n**0.5)+1):
		divisors[k**2] = divisors [k**2] + [(k,k)]
	return divisors
 
limit = 10**6
divisors = divisorsList(limit)
compte = 0
for n in xrange(2,limit):
	if len(divisors[n])<5: 
		continue
	temp = 0
	for div in divisors[n]:
		d1, d2 = div
		if (3*d1-d2) % 4 == 0 :
			if 3*d2-d1>0 and d1!=d2 : 
				temp+=2
		else: 
			temp+=1
		if temp>10: 
			break
	if temp==10: 
		compte+=1
print compte