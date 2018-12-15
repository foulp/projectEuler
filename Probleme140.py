"""Probleme 140"""
limit = 30
total = 0
nuggets = []
start = [(0,1),(0,-1),(-3,2),(-3,-2),(-4,5),(-4,-5),(2,7),(2,-7)]
for s in start:
	x,y = s
	for i in xrange(limit):
		x,y = -9*x-4*y-14, -20*x-9*y-28
		if x>0 and x not in nuggets:
			total+=x
			nuggets.append(x)
			print x
nuggets.sort()
total = sum(nuggets[:limit])
#n = 1
#compte = 1
#while compte<limit:
#          delta = (n+1)**2 + 4*n*(n+3) #= n**2 + 2*n + 1 + 4*n**2 + 12*n = 5*n**2 + 14*n + 1 = (7*n+1)**2 - 11*(2*n)**2
#          if int(delta**0.5)**2 == delta:
#                      total+=n
#                      compte+=1
#                      print compte, n, delta**0.5-(n+1), 2*(n+3)
#          n+=1
print "Total is:", total