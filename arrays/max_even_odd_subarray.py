def max_even_odd_subarray(arr):

     c=1
     res=1

     for i in range(1,len(arr)):

          if arr[i]%2==0:
               f=0
          else:
               f=1
          e=arr[i-1]%2

          
          if e!=f:
               c+=1
               if res<c:
                    res=c
          else:
               c=1
     return res

print(max_even_odd_subarray([1,4,5,6,7,3,0,3,2,4,8,6,1]))

               
               
               
