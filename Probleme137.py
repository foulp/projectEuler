"""Probleme 137"""
from fractions import gcd

limit = 15
total = 0
p = 2
q = 1
which = 0

while total<limit:
	if gcd(p,q)==1 and p%2!=q%2:
		x = (which==0)*(p*p - q*q) + (which==1)*(2*p*q)
		y = (which==1)*(p*p - q*q) + (which==0)*(2*p*q)
		print (which==0)*(x-1) + (which==1)*max(x,y)
		total +=1
	if total==limit: break
	while True:
		p+=1
		test = (5*p*p-4)**0.5
		if int(test) == test:
			q = (-p + test) / 2
			which = 0
			break
		test = (5*p*p+1)**0.5
		if int(test) == test:
			q = -2*p + test
			which = 1
			break

print total