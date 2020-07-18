def largestAndSecondLargest(sizeOfArray, arr):

    check=arr[0]
    flag=False
    for i in arr:
        if i!=check:
            flag=True
            break
    if not flag:
        return [check,-1]
        
    else:
        lar,sl=0,0
        for i in range(sizeOfArray):
            if arr[i]>lar:
                sl=lar
                lar=arr[i]
            elif arr[i]>sl:
                print(arr[i])
                
                if arr[i] != lar:
                    
                    sl=lar

        return [lar,sl]

print(largestAndSecondLargest(3,[2,1,2]))
