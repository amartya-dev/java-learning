def change_array(arr,smallest_index):

     try:
          if arr[smallest_index+1]==0:
               arr[smallest_index+1]=arr[smallest_index]+1
     except IndexError:
          pass

     try:
          if arr[smallest_index-1]==0:
               arr[smallest_index-1]=arr[smallest_index]+1
     except IndexError:
          pass
     return arr
     

     
def mudwallthingy(pos,heights):

     arr=[0 for i in range(pos[-1])]

     for i in range(len(pos)):
          arr[pos[i]-1]=heights[i]
     #print(arr)

     while True:
          smallest_index=0
          smallest=9999
          for i in range(len(arr)):

               if i==0:
                    
                    
                    if arr[i]!=0 and arr[i+1]==0 and arr[i]<smallest:
                         #print('yes')
                         smallest_index=i
                         smallest=arr[i]

               elif i==len(arr)-1:
                    if arr[i]!=0 and arr[i-1]==0 and arr[i]<smallest:
                         smallest_index=i
                         smallest=arr[i]
               
               elif arr[i]<smallest and (arr[i-1] ==0 or arr[i+1]==0) and arr[i]!=0:
                    #print(i)
                    smallest_index=i
                    smallest=arr[i]
          #print(smallest_index)
          if smallest==9999:
               break

          arr=change_array(arr,smallest_index)
          #print(arr)

     return arr
          
          
          
               
          
print(mudwallthingy([1,2,4,7],[4,6,8,11]))
     
