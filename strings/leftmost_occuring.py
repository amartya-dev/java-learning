def leftmost_occuring(s1):

     g=set(s1)
     if len(g)==len(s1):
          return -1


     chars = [0 for i in range(256)]

     for i in range(len(s1)):

          chars[ord(s1[i])]+=1

     for i in range(len(chars)):
          if chars[i]>1:
               repeating=chr(i)
               break
     else:
          return -1
     print(chars)
     return s1.find(repeating)
     

print(leftmost_occuring('abdhggcccc'))
