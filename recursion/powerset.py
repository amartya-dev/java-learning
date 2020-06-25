ff=[]

def powset(s):
     global ff
     print(s)
     ff.append(s)
     if s=='':
          return ''
     v=powset(s[1:])
     ff.append(v)
     return s[0]+v
powset('abc')
print(ff)
