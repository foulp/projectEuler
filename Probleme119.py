power = [[k,k] for k in xrange(2,100)]
limit = 30
compteur, nombres = 0, []
while compteur<limit:
   power[0] = [power[0][0]*power[0][1], power[0][1]]
   if sum([int(d) for d in str(power[0][0])])==power[0][1]:
      compteur+=1
      nombres.append(power[0])
   power.sort()
 
print nombres[-1][0]