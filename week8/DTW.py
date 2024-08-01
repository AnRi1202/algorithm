def dist(x,y):
  return (x-y)**2
def dtw(a,b):
  N = len(a)
  M = len(b)
  
  dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
  dp[0][0] = dist(a[0],b[0])
  for i in range(1,N):
    dp[i][0] = dp[i-1][0] + dist(a[i],b[0])
  for j in range(1,M):
    dp[0][j] = dp[0][j-1] + dist(a[0],b[j])
  for i in range(1,N):
    for j in range(1,M):
      dp[i][j] = dist(a[i],b[j]) + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
  return dp[N-1][M-1]

a = [1,2,3,4,5]
b = [2,3,4,5,6]
print(dtw(a,b))