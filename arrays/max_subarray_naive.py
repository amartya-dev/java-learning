final=[]

def max_subarray(arr,n):
     global final

     if n==1:
          #print(arr[0])
          return arr[0]
     x=max(max_subarray(arr[:-1],n-1)+arr[-1],arr[-1])
     #print(x)
     final.append(x)
     return x

def execute(arr,n):
     max_subarray(arr,n)
     return max(final)
     
print(execute([1,-2,3,-5,6,-6,-1,2],8))     

