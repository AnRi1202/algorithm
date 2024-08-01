def create_table(pattern):
  table = [0] * len(pattern) -1
  j = 0
  for i in range(1, len(pattern)-1):
    if pattern == pattern[j]:
      j += 1
      table[i] = j
    else:
      while j > 0:
        j = table[j-1]
        if pattern[i] == pattern[j]:
          j += 1
          table[i] = j
          break
        

def kmp(text, pattern):
  skip = create_table(pattern)
  t_len = len(text)
  p_len = len(pattern)
  t_i = 0
  p_i = 0
  while t_i < t_len and p_i < p_len:
    if text[t_i] == pattern[p_i]:
      t_i += 1
      p_i += 1
    else:
      p_i = skip[p_i]
  if p_i == p_len:
    return t_i - p_i
  else:
    return -1

text = "ababcababcabcabc"
pattern = "abcabc"
print(kmp(text, pattern))