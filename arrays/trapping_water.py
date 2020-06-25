def trapping_water(arr):


     #pre find left and right max for each position 
     leftmax=[arr[0]]
     for i in range(1,len(arr)):
          x=max(leftmax[-1],arr[i])
          leftmax.append(x)

     rightmax=[arr[-1]]
     for i in range(len(arr)-2,-1,-1):
          print(arr[i])
          x=max(rightmax[0],arr[i])
          rightmax.insert(0,x)

     print(rightmax,leftmax)
     tot=0
     for i in range(1,len(arr)-1):
          tot+=min(rightmax[i],leftmax[i])-arr[i]

     return tot







               
          
          
          
               

print(trapping_water([5,0,6,2,3]))
