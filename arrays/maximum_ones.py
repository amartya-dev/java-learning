def maximum_ones(arr):

     c=0
     res=0
     for i in range(len(arr)):

          if arr[i]==0:
               c=0
          else:
               c+=1
               if c>res:
                    res=c
     return res
print(maximum_ones([0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,1,0]))
