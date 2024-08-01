amount = 25
coins = [1, 8, 13]
dp = [0 for i in range(amount+1)]
for i in range(1, amount+1):
  tmp_min = 10**6
  for j in range(len(coins)):
    if(i -coins[j] > -1) and (tmp_min > dp[i -coins[j]]):
      tmp_min = dp[i -coins[j]]
  dp[i] = tmp_min + 1
  
print(dp[amount])
