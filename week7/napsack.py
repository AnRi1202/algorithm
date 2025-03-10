W = 15
N = 6
weight = [11, 2, 3, 4, 1, 5]
value = [15, 3, 1, 4, 2, 8]

dp = [[-1 for _ in range(W+1)] for _ in range(N+1)]

for i in range(W + 1):
  dp[0][i] = 0
  
for i in range(N):
  for j in range(W+ 1):
    if weight[i] <=j:
      dp[i+1][j] = max(dp[i][j], dp[i][j -weight[i]] + value[i])
    else: dp[i+1][j] = dp[i][j]
    
print(dp[N][W])