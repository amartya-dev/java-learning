def ways_to_coin_change(coins, n, s):

     if s == 0:
          return 1
     if n == 0:
          return 0
     

     res = ways_to_coin_change(coins, n-1, s)

     if coins[n-1] <= s:

          res += ways_to_coin_change(coins,n, s - coins[n-1])
     return res


print(ways_to_coin_change([1,2,3],3,4))
