def isBouncy(n):
   digits = [int(d) for d in str(n)]
   k=0
   while digits[k]==digits[k+1]:
      k+=1
      if k==len(digits)-1:
         return False
   down = digits[k]>digits[k+1]
   for i in range(k+1, len(digits)-1):
      if digits[i]==digits[i+1]:
         pass
      elif (digits[i]>digits[i+1])!=down:
         return True
   return False
  
ratio = 0.99
k, compte = 99, 0.0
while compte/k<ratio:
   k+=1
   if isBouncy(k):
      compte+=1
 
print k