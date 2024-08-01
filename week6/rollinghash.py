def RollingHashMatch(text, pattern):
  t_len = len(text)
  p_len = len(pattern)
  base = 256
  mod = 101
  t_hash = 0
  p_hash = 0
  h = 1
  for i in range(p_len-1):
    h = (h * base) % mod
  for i in range(p_len):
    t_hash = (base * t_hash + ord(text[i])) % mod
    p_hash = (base * p_hash + ord(pattern[i])) % mod
  for i in range(t_len - p_len + 1):
    if t_hash == p_hash:
      for j in range(p_len):
        if text[i+j] != pattern[j]:
          break
      if j == p_len - 1:
        return i
    if i < t_len - p_len:
      t_hash = (base * (t_hash - ord(text[i]) * h) + ord(text[i+p_len])) % mod
      if t_hash < 0:
        t_hash += mod
  return -1

text = "ababcababcabcabc"
pattern = "abcabc"

print(RollingHashMatch(text, pattern))