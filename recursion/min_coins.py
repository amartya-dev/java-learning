final=[]
def minimum_coins(tar,coins,s=[]):
     
     global final
     if tar==0:
          final.append(s)
          #print(s)
          return 1
     if tar<0:
          s=[]
          return 0
     

     x=[]
     for i in coins:
          
          x.append(minimum_coins(tar-i,coins,s+[str(i)]))
     
     
def calculate(tar, coins):

     minimum_coins(tar, coins)
     #print(final)
     x=final[0]
     for i in range(1,len(final)):
          if len(final[i])<len(x):
               x=final[i]
     return (x,len(x))
          
          
          
print(calculate(63,[1,65]))

   
'''

3,(2,1,0)
2,(1,0,-1)
1,(0,-1,-2)


     
minimum_coins(12,[1,2,3])'''
