# 0<=x<10**1 : 0
 
# 10**1<=x<10**2 : x1/x2 pair/impair ou impair/pair sans retenue
# x1 = 1 : x2 in [2,4,6,8]
# x1 = 2 : x2 in [1,3,5,7]
# x1 = 3 : x2 in [2,4,6]
# x1 = 4 : x2 in [1,3,5]
# x1 = 5 : x2 in [2,4]
# x1 = 6 : x2 in [1,3]
# x1 = 7 : x2 in [2]
# x1 = 8 : x2 in [1]
# x1 = 9 : x2 in []
### Total = 20
 
#10**2<=x<10**3 : x1/x3 pair/impair ou impair/pair avec retenue et 2*x2+1 sans retenue ie x2<=4 ie x2 in [0,1,2,3,4]
# x1 = 1 : x3 in []
# x1 = 2 : x3 in [9]
# x1 = 3 : x3 in [8]
# x1 = 4 : x3 in [9,7]
# x1 = 5 : x3 in [8,6]
# x1 = 6 : x3 in [9,7,5]
# x1 = 7 : x3 in [8,6,4]
# x1 = 8 : x3 in [9,7,5,3]
# x1 = 9 : x3 in [8,6,4,2]
### Total = 20*5 = 100
 
#10**3<=x<10**4 : x1/x4 pair/impair ou impair/pair sans retenue et x2/x3 pair/impair ou impair/pair sans retenue
# x1 = 1 : x4 in [2,4,6,8]
   # x2 = 0 : x3 in [1,3,5,7,9]
   # x2 = 1 : x3 in [0,2,4,6,8]
   # x2 = 2 : x3 in [1,3,5,7]
   # x2 = 3 : x3 in [0,2,4,6]
   # x2 = 4 : x3 in [1,3,5]
   # x2 = 5 : x3 in [0,2,4]
   # x2 = 6 : x3 in [1,3]
   # x2 = 7 : x3 in [0,2]
   # x2 = 8 : x3 in [1]
   # x2 = 9 : x3 in [0]
   ### Total = 4*30 = 1200
# x1 = 2 : x4 in [1,3,5,7]
   ### Total = 4*30 = 1200
# x1 = 3 : x4 in [2,4,6]
   ### Total = 3*30 = 90
# x1 = 4 : x4 in [1,3,5]
   ### Total = 3*30 = 90
# x1 = 5 : x4 in [2,4]
   ### Total = 2*30 = 60
# x1 = 6 : x4 in [1,3]
   ### Total = 2*30 = 60
# x1 = 7 : x4 in [2]
   ### Total = 1*30 = 30
# x1 = 8 : x4 in [1]
   ### Total = 1*30 = 30
# x1 = 9 : x4 in []
   ### Total = 0*30 = 0
### Total = 20*30 = 600
 
#10**4<=x<10**5 : x1/x5 pair/impair ou impair/pair, x2/x4 avec retenue, x2/x4 sans retenue
### Total = 0
 
#10**5<=x<10**6 : x1/x6 pair/impair ou impair/pair sans retenue, x2/x5 pair/impair ou impair/pair sans retenue, x3/x4 pair/impair ou impair/pair sans retenue
### Total = 20*30*30 = 18000
 
#10**6<=10**7 : x1/x7 pair/impair ou impair/pair avec retenue, x2/x6 pair/pair ou impair/impair sans retenue, x3/x5 impair/pair ou pair/impair avec retenue, x4/x4 sans retenue
### Total = 20*(5+4+4+3+3+2+2+1+1+0)*20*5 = 50000
 
#10**7<=x<10**8 : x1/x8 pair/impair ou impair/pair sans retenue, x2/x7 pair/impair ou impair/pair sans retenue, x3/x6 pair/impair ou impair/pair sans retenue, x4/x5 pair/impair ou impair/pair sans retenue
### Total = 20*30**3 = 540000
 
#10**8<=x<10**9 : x1/x9 pair/impair ou impair/pair, x2/x8 sans retenue, x3/x7 pair/impair ou impair/pair, x4/x6 sans retenue, x5/x5 PROBLEME
### Total = 0
 
print "GRAND_TOTAL = 20+100+600+0+18000+50000+540000+0 = 608720"