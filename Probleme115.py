"""Probleme 115"""
m = 50
scores = {size:1 for size in xrange(m)}
n = m-1
while scores[n]<=10**6:
   n+=1
   total = scores[n-1]
   for tileSize in xrange(m,n):
      total += scores[n-(tileSize+1)]
   scores[n] = total+1
print "Answer is :",n, scores[n]