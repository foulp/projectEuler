def fact(n):
   if n<=1:
      return 1
   else:
      return n*fact(n-1)
     
def max_prize(n):
   outcomes = fact(n+1)
   incomes = [1]
  
   for i in range(1,n+1):
      temp = [[0]]*(i+1)
     
      temp[0] = incomes[0]*i
      for k in range(1,i):
         temp[k] = incomes[k]*i+incomes[k-1]
      temp[i] = incomes[i-1]
 
      incomes = [val for val in temp]
  
   return int(float(outcomes)/sum(incomes[n//2+1:]))
     
print max_prize(15)