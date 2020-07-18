n=int(input())
for i in range(n):
    x=input()
    
    c=[]
    for i in range(len(x)):
        
        if x[i].isdigit():
            try:
                if c[-1].isdigit():
                    c[-1]+=x[i]
                else:
                    c.append(x[i])
            except IndexError:
                c.append(x[i])
        else:
            c.append('.')

    m=0
    #print(c)
    for i in c:
        try:
            m+=int(i)
        except:
            pass
    print(m)
            

            
