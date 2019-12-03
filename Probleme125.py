def sumConsecutiveSquares(n):
   top = int(n**0.5)
   if top**2==n:
      top-=1
   for i in range(1, top+1):
      somme, k = i**2, i
      while somme<n:
         k+=1
         somme+=k**2
      if somme==n:
         return True
   return False
  
somme = 0
for k in range(1,9):
   if k==1:
      for n in range(2,10):
         if sumConsecutiveSquares(n):
            somme += n
   elif k%2==0:
      for i in range(10**(k//2-1), 10**(k//2)):
         n = int(str(i)+str(i)[::-1])
         if sumConsecutiveSquares(n):
            somme += n
   elif k%2==1:
      for i in range(10**(k//2-1), 10**(k//2)):
         for j in range(10):
            n = int(str(i)+str(j)+str(i)[::-1])
            if sumConsecutiveSquares(n):
               somme += n
print somme
