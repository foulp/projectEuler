from fractions import gcd
 
pmax, kmax = 20, 15
triplets = []
for p in xrange(2,pmax+1):
   for q in xrange(1+p%2,p,2):
      if gcd(p,q)==1:
         for k in xrange(1,kmax+1):
            triplets.append([k*(p**2+q**2), k*(2*p*q), k*(p**2-q**2)])
 
triplets.sort()
found = []  
for t in triplets:
   d,f,b = t
   edge = 0
   while triplets[edge][0]<=d:
      edge+=1
      if edge>=len(triplets):
         break
 
   for t1 in triplets[edge:]:
      if f<t1[1] and b==t1[2] :
         c,e,_ = t1
         a = (c**2+f**2)**0.5
         if int(a)==a:
            found.append([(c**2+d**2)/2, (e**2+f**2)/2, (c**2-d**2)/2])
              
      if d<t1[2] and f==t1[1]:         
         a,_,c = t1
         e = (a**2-d**2)**0.5
         if int(e)==e:
            found.append([(a**2+b**2)/2, (a**2-b**2)/2, (c**2-d**2)/2])
  
print min([sum(collect) for collect in found])