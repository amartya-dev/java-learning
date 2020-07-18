n = 7
memo = [-1 for i in range(n+1)]

def fibonacci(n):

     if memo[n] == -1:

          if n == 0 or n == 1:
               res = n
          else:
               return fibonacci(n-1) + fibonacci(n-2)
          memo[n] = res
          return res
     else:
          return memo[n]

print(fibonacci(n))
