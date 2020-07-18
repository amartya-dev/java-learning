def subsring(f):

     x=[1 for i in range(len(f))]

     for i in range(len(f)):
          for j in range(i+1,len(f)):
               if f[j]>f[j-1]:
                    
                    x[i]+=1
               else:
                    break
     #print(x)
     return max(x)

print(subsring([1,10,5,3,0,4,6,8]))
