'''def maxConsecutiveOnes(x):
    ##Your code here
    s=0
    a=x
    o=[]
    l=a&~(a-1)
    while a>0:
        #print(a)
        b=a^l
        #print(b)
        #print(l)
        
        if b>a:
            b=a
            o.append(s)
            s=0
            l=a&~(a-1)
        else:
            a=b
            s+=1
            l=l<<1
    #print('______________________________')
    o.append(s)
    return max(o)'''

def maxConsecutiveOnes(x):
    ##Your code here
    count = 0
    while x!=0:
        x = x & (x<<1)
        count+=1
        
    return count
   
print(maxConsecutiveOnes(30957))
