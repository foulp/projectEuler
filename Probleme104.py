from math import log10
 
phi = log10((1+5**0.5)/2)
log = log10(5**0.5)
 
a, b = 1, 1
compte = 2
digits = set([str(d) for d in range(1,10)])
found = False
while found==False:
   a, b = b, (a+b)%(10**9)
   compte+=1
   if set(str(b))==digits:
      test = compte*phi-log
      test = int(10**(test-int(test)+8))
      if set(str(test))==digits:
         found = True
     
print compte