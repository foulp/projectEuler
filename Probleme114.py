"""Probleme 114"""
scores = {0:1,1:1,2:1}
n = 50
for size in xrange(3,n+1):
print size
total = scores[size-1]
for tileSize in xrange(3,size):
total += scores[size-(tileSize+1)]
scores[size] = total+1
print "Answer is :", int(scores[n])