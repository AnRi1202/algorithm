def brute_force(text, pattern):
  t_len = len(text)
  p_len = len(pattern)
  
  t_i  = 0
  p_i = 0
  while t_i < t_len and p_i < p_len:
    if text[t_i] == pattern[p_i]:
      t_i += 1
      p_i += 1
    else:
      t_i -= p_i - 1
      p_i = 0
  if p_i == p_len:
    return t_i - p_i
  else:
    return -1

text = "ababcababcabcabc"
pattern = "abcabc"
print(brute_force(text, pattern))