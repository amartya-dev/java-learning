def ways_to_coin_change_loop(coins, n, s):

     dp = [[-1 for i in range(n+1)] for j in range(s+1)]

     for i in range(n):
          dp[0][i] = 1

     for j in range(1,s):
          dp[i][0] = 0

     for i in range(1,s+1):
          for j in range(1,n+1):
               dp[i][j] = dp[i][j-1]
               if coins[j-1]<=i:
                    dp[i][j] += dp[i-coins[j-1]][j]
     print(dp)
     return dp[s][n]

print(ways_to_coin_change_loop([1,2,3],3,4))
                    
     
     
