def lh_pattern(arr):
     c=0
     #LHLHLH
     for i in range(len(arr)-1):
          if i==0 and arr[i+1]<arr[i]:
               arr[i]=arr[i+1]-1
               

     
          if i%2!=0:
               #H
               if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
                    continue
               else:
                    arr[i]=max(arr[i-1],arr[i+1]) +1
                    c+=1
                    
          else:
               #L
               if arr[i]<=arr[i-1] and arr[i]<=arr[i+1]:
                    continue
               else:
                    c+=1
                    arr[i]=min(arr[i-1],arr[i+1]) -1

     if (len(arr)-1)%2==0:
          if arr[-1]>arr[-2]:
               arr[-1]=arr[-2]-1
               c+=1
     else:
          if arr[-1]<arr[-2]:
               c+=1
               arr[-1]=arr[-2]+1
     #print(c)
     return c

def hl_pattern(arr):
     c=0
     #HLHLHLH
     for i in range(len(arr)-1):
          if i==0 and arr[i+1]>arr[i]:
               arr[i]=arr[i+1]+1
               

     
          if i%2!=0:
               #L
               if arr[i]<=arr[i-1] and arr[i]<=arr[i+1]:
                    continue
               else:
                    arr[i]=min(arr[i-1],arr[i+1]) -1
                    c+=1
                    
          else:
               #H
               if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
                    continue
               else:
                    c+=1
                    arr[i]=max(arr[i-1],arr[i+1]) +1

     if (len(arr)-1)%2==0:
          if arr[-1]<arr[-2]:
               arr[-1]=arr[-2]+1
               c+=1
     else:
          if arr[-1]>arr[-2]:
               c+=1
               arr[-1]=arr[-2]-1
     #print(c)
     return c
               

def wavepatternarray(arr):

     #LHLHLH
     return min(lh_pattern(arr),hl_pattern(arr))

print(wavepatternarray([2,1,2,3,4,5,2,9]))
