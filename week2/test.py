#S行列に和を作っておく
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

Sxi = [0] * (N+1)
Sx = [0] * (N+1)
sum = 0
for i in range(N): 
  sum += x[i] * (i+1)
  Sxi[i+1] = sum

sum = 0
for i in range(N):
  sum += x[i]
  Sx[i+1] = sum

for i in range(Q):
  sum = (Sxi[R[i]] - Sxi[L[i]-1])* A[i] + B[i]*(Sx[R[i]]-Sx[L[i]-1])
  print(sum)
  
  