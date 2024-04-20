
#素数の数え上げ
def seq_prime_all(n):
  seq_prime_List = [0] * (n+1)
  is_prime=[True]*(n+1)
  i=2
  while(i*i<=n):
    if(is_prime[i]):
      j=i*i
      while(j<=n):
        is_prime[j]=False
        j+=i
    i+=1
  sum = 0
  #is_primeがTrueであるNについて、N+1/2が素数であるかを判定する
  for i in range(3,n+1):
    if is_prime[i] and is_prime[(i+1)//2]:
      sum+=1
    seq_prime_List[i-1]= sum
  return seq_prime_List

#seq_prime_all(10)のリストを表示
  
#+1は2が条件を満たすので別途考えた

Q = int(input())
result = seq_prime_all(10**3+1)
L = [0] * Q
R = [0] * Q
for i in range(Q):
  L[i], R[i] = map(int, input().split())
  
for i in range(Q):
  print(result[R[i]] - result[L[i]-1])
