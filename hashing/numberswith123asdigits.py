
t = int(input())

reference = {'1','2','3'}


for tc in range(t):
    
    n = int(input())
    a = list(map(str,input().strip().split()))
    
    found = False
    #print(a)
    for i in a:
        
        val = set(i)
        #print(val)
        if val.issubset(reference):
            found = True
            print(i, end = ' ')
        
    if not found:
        print(-1)
