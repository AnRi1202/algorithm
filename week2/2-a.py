n = 10
k = 3


#n! % M O(n) ##finish
def factorial_surplus(n, M):
    result = 1
    for i in range(1, n+1):
        if result % M != 0:
          result = (i*result)% M
        else:
          result = 0
          break
    return result


#N^m % M O(n) ##yet
def exp_mod(N, m, M):
  result = 1
  if(m == 0):
    return 1
  while(m>0):
    if(m%2 == 1):
      result = (result * N) % M
    N = (N * N) % M
    m = m//2
  return result    
#998244353
#18289152000
#nCk % M  ##yet

def combination_surplus(n,k,M):
  reuslt = 1
  n_f=factorial_surplus(n,M)

  nk_f=factorial_surplus(n-k,M)

  k_f=factorial_surplus(k,M)
  return(n_f*exp_mod(nk_f,M-2,M)*exp_mod(k_f,M-2,M))%M

print(combination_surplus(n,k,998244353))



