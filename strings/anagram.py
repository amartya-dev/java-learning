def anagrams(s1,s2):
     if len(s1) != len(s2):
          return False

     chars = [0 for i in range(256)]

     for i in range(len(s1)):

          chars[ord(s1[i])]+=1

     for i in range(len(s2)):

          chars[ord(s2[i])]-=1

     if sum(chars) == 0:
          return True
     else:
          return False
     

print(anagrams('acabbc','bbaac'))
