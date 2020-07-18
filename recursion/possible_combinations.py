final=[]
def possible_combinations(s,tot=''):

     global final
    
     if len(s)==1:
          
          final.append(tot+s)

     for char_index in range(len(s)):
          temp=list(s)
          del temp[char_index]
          h= ''.join(temp)
          possible_combinations(h,tot+s[char_index])

possible_combinations('abc')
print(final)
          



