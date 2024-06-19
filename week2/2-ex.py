N = int(input())
x = map(int,input().split())
x = list(x)
Q = int(input())
L = [0] * Q
R = [0] * Q
A = [0] * Q
B = [0] * Q
for i in range(Q):
  L[i], R[i],A[i],B[i] = map(int, input().split())



y = [x[i] * (i+1) for i in range(N)]  
for i in range(Q):
  sum = 0
  for j in range(L[i]-1,R[i]):
    sum += y[j] * A[i] + x[j]*B[i]
  print(sum)