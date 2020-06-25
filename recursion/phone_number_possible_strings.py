final=[]
refer={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
##Complete this function
def possibleWords(a,N,index=0,s=''):
    ##Your code here
    
    if index==N:
        final.append(s)
        print(s, end=' ')
        return
    
    possible_chars=refer[a[0]]
    for i in possible_chars:
        
        s+= i
        possibleWords(a[1:],N,index+1,s)
        s=s[:-1]
        
            
        
    
