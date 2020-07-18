import math
import os
import random
import re
import sys

# Complete the stringSimilarity function below.
def get_suffix(s):
    return s[1:]
def stringSimilarity(s):

    if len(s)==1:
        return 1

    count=0
    possible_strings=[s]

    #ababaa
    #babaa
    #abaa
    #baa
    #aa
    #a
    
    for i in range(len(s)-1):
        possible_strings.append(get_suffix(possible_strings[-1]))

    x=possible_strings.pop(0)
    x=len(x)
    
    for string in possible_strings:
    
        i=0
        while i<len(string):
            if string[i]==s[i]:
                count+=1
            else:
                break
            i+=1
    return count+x

        



if __name__ == '__main__':


    t = int(input())

    for t_itr in range(t):
        s = input()

        result = stringSimilarity(s)

        print(result)
