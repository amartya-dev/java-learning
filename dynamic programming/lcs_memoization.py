m = 4
n = 4
memo = [[-1 for i in range(n+1)] for j in range(m+1)]

def lcs(s1,s2,m,n):

     if memo[m][n] !=-1:
          return memo[m][n]

     if m == 0 or n == 0:
          memo[m][n] = 0
     elif s1[m-1] == s2[n-1]:
          memo[m][n] = 1 + lcs(s1,s2,m-1,n-1)
     else:
          memo[m][n] = max(lcs(s1,s2,m-1,n),lcs(s1,s2,m,n-1))
     return memo[m][n]
print(lcs('abcd','acbd',m,n))
