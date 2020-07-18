def binarySubstring(n,s):
    #code here
    
    low = 0
    high = n-1
    
    count = 0
    
    while low<high:
         
        
        while True:
            if s[low]=='1':
                break
            low+=1
        
        while low<high:
             
            print(low,high,count) 
            try:
                if s[high]=='1':
                    count+=1
                high-=1
                if high-low==1:
                    low+=1
                    high=n-1
            except:
                print("error: ",high)
                break
    return count


print(binarySubstring(8,'00100101'))
