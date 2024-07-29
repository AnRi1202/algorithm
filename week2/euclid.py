def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a%b)

## 計算によってax + by = 1の解を求める
def ext_gcd(a,b):
  if b== 0:
    return a, 1, 0
  else:
    d, x, y = ext_gcd(b, a%b)
    return d, y , x- (a//b)*y