N = 30

##################
#  Nim games
#  n^(2*n)^(3*n) = 0 <=> .. <=> n & (2*n) = 0 <=> no consecutives 1s in n
#  Using Fibonnaci
#  For binary of length n: X(n) = X(n-1) + X(n-2)

fibo = [1, 1]
for n in xrange(1, N + 1):
	fibo.append(sum(fibo[-2:]))
print fibo[-1]