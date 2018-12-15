def isPrime(n):
   if n<=1:
      return False
   if n in [2,3,5,7]:
      return True
   if n%10 in [0,2,4,5,6,8]:
      return False
   for i in range(3,int(n**0.5)+1,2):
      if n%i==0:
         return False
   return True
 
p, n = 2, 1
while n<=7037:
   p+=1
   while isPrime(p)==False:
      p+=1
   n+=1
  
limit = 10
while True: 
   if len(str( ((p-1)**n+(p+1)**n) % (p**2) ))>limit:
      break
   p+=1
   while isPrime(p)==False:
      p+=1
   n+=1
  
print n