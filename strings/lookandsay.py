def next_number(s):
     result=[]
     i=0
     while i<len(s):
          c=1
          while i+1<len(s) and s[i]==s[i+1]:
               i+=1
               c+=1
          result.append(str(c)+s[i])
          i+=1
     return ''.join(result)

x=int(input())
for i in range(x):
     m=int(input())
     for x in range(1,m+1):
          l=next_number(str(m))
     print(l)
               
