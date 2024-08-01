def bm_search(text,pattern):
  t_len = len(text)
  p_len = len(pattern)
  skip = [p_len] * 26
  for i in range(p_len-1):
    skip[ord(pattern[i]) - ord('a')] = p_len - i - 1
    
  t_i = p_len - 1
  while t_i < t_len:
    p_i = p_len - 1
    while text[t_i] == pattern[p_i]:
      if p_i == 0:
        return t_i
      t_i -= 1
      p_i -= 1
    t_i += max(skip[ord(text[t_i]) - ord('a')], p_len - p_i)
  return -1

text = "ababcababcabcabc"
pattern = "abcabc"

print(bm_search(text, pattern))