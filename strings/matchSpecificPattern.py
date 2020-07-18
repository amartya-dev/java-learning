#Function should return a list/array containing the required words

''' The function returns a  list of strings 
present in the dictionary which matches
the string pattern.
You are required to complete this method '''

def findSpecificPattern(Dict, pattern):
    #Code here
    #print(Dict)
    ans=[]
    for i in Dict:
        if len(i)==len(pattern):
            d={}
            same=True
            for l in range(len(i)):
                #print(i[l], '&',pattern[l])
                if i[l] not in d and pattern[l] not in d.values():
                    d.update({i[l]:pattern[l]})
                    #print(d)
                else:
                    #print(i[l]," is ",d[i[l]])
                    try:
                        if d[i[l]]!=pattern[l]:
                            same=False
                    except:
                        same=False
                    
            if same:
                #print(i)
                ans.append(i)
            #break
        #print('__________________________')
    #print(pattern)
    return ans
