def max_sum(a):
  s = [0]* (len(a)+1)
  for i in range(len(a)):
    s[i+1] = max(s[i]+a[i], a[i])
  
  return s[len(a)]
