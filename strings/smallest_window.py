def smallestWindow(s, P):
    #code here
    n = len(s)
    m = len(P)
    low = 0
    high = 0
    i,j = 0,0
    missing = m
    pat_hash = [0 for i in range(256)]
    print(pat_hash)
    for k in P:
        pat_hash[ord(k)] += 1
    print(pat_hash)

        
    while high<n:

        if pat_hash[ord(s[high])] > 0:
             #print(pat_hash)
             missing -= 1
        pat_hash[ord(s[high])] -= 1
             
        high += 1
            
            
            
        while missing == 0:
            
            if j == 0 or j-i > high-low:
                i,j = low,high
            
            pat_hash[ord(s[low])] += 1
            
            if pat_hash[ord(s[low])] > 0:
                missing += 1
            low += 1
    print('\n\n',i,j)
    return s[i:j]

print(smallestWindow('timetopractice','toc'))
