def subsetsumproblem(arr,s,index,g=[0]):

     if index==0:
          if sum(g)==s:
               return 1
     return subsetsumproblem(arr,s,index-1, g)+subsetsumproblem(arr,s,index-1,g.append(arr[index-1]))

arr=[1,2,3,4,5]
s=5
print(subsetsumproblem(arr,s,5))
