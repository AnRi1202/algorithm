#掛け算
def power(x, n):
  M = 10**9 + 7
  if n ==0:
    return 1
  
  tmp = power(x*x % M, n//2)
  if n % 2:
    tmp = tmp * x % M
    
  return tmp

#割り算