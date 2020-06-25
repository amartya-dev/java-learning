def stock_buy_sell(a):
     x=[[]]
     for i in range(len(a)-1):
          if a[i+1]>a[i]:
               x[-1].append(a[i])
          else:
               if len(x[-1])!=0:
                    
                    x[-1].append(a[i])
               x.append([])
     try:
          
          if x[-1][-1]<a[-1]:
               x[-1].append(a[-1])
     except:
          pass
     tot=0
     for i in x:
          if len(i)>0:
               tot+=i[-1]-i[0]
               
          
     return tot
print(stock_buy_sell([1,5,3,1,2,8,3,50]))
