def fib_rev1(n):
  f = [0]*(n+1)
  def fib(n):
    if n <= 2:
      return 1
    elif f[n] != 0:
      return f[n]
    else:
      f[n] = fib(n-1) + fib(n-2)    
    return f[n]
  return fib(n)
    
    
print(fib_rev1(9))

def fib_rev2(n):
  if n <= 2:
    return 1
  else:
    f = [0]*(n+1)
    f[0] = 0
    f[1]  =1
    f[2] = 1
    for i in range(3, n+1):
      f[i] = f[i-1] +f[i-2]
  return f[n]
    
print(fib_rev2(9))