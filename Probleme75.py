from fractions import gcd

limit=1500000
perimeter={}

for m in range(2,int((limit/2)**0.5)+1):
    for n in range(m%2+1,m,2):  
        if gcd(m,n)==1:
            a,b,c = m**2-n**2, 2*m*n, m**2+n**2
            peri=2*m*(m+n)
            k=1
            while k*peri<=limit:
                if k*peri in perimeter.keys():
                    perimeter[k*peri]+=1
                else:
                    perimeter[k*peri]=1
                k+=1
                

temp=[value for value in perimeter.values() if value==1]
print(len(temp))


#Answer is 161667