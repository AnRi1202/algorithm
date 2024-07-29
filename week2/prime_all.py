#エラストテネスの篩
def prime_all(n):
  
  is_prime = [True]*(n+1)
  is_prime[0], is_prime[1] = False, False 
  i = 2
  while i*i <= n:
    if is_prime[i]:
      for j in range(i*i, n+1, i):
        is_prime[j] = False
    i += 1  
  return len([i for i in range(2, n+1) if is_prime[i]])


n = int(input())
print(prime_all(n))


#SPFの求め方 最小の素因数のこと
def spf(n):
  spf = [_ for  _ in range (n+1)]
  i = 2
  while i*i <= n:
    if spf[i] == i:
      j = 2*i
      while j <= n:
        if spf[j] == j:
          spf[j] = i
          j += i
    i += 1
  return spf

def PrimeFactorizaion(n):
  spf_table = spf(n)
  while n > 1:
    print(spf_table[n])
    n //= spf_table[n]