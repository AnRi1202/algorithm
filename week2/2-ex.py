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

for i in range(Q):
  sum = 0
  for j in range(L[i]-1,R[i]):
    sum += x[j] * (A[i] *(j+1)+B[i])
  print(sum)