def ascending_check(arr,n):
    smallest=arr[0]
    small_index=0
    for i in range(1,n):
        if arr[i]<smallest:

            smallest=arr[i]
            small_index=i

    print(small_index)
    ascending=True
    for j in range(n-1):

        if arr[small_index]>arr[(small_index+ 1)%n]:
            ascending=False
            break
        small_index+=1
        small_index=small_index%n
    #print(ascending)
    if ascending:
        if arr[0]>=arr[n-1]:
            return True
        else:
            return False

print(ascending_check([29, 29, 33, 33, 41, 48, 49, 57, 77, 88, 10, 11, 11, 23, 29, 29],16))
