def posOfRightMostDiffBit(m,n):
    #Your code here
    i=1
    p=1
    if m==n:
        print(-1)
    while True:
        x=m&i
        y=n&i
        if x^y==0:
            i=i<<1
            p+=1
            continue
        else:
            return p
    

