def qsort(seq, left, right):
  if right <= left:
    return
  pivot = seq[right]
  i = left
  for j in range(left, right):
    if seq[j] < pivot:
      seq[i], seq[j] = seq[j], seq[i]
      i += 1
  seq[i], seq[right] = seq[right], seq[i]
  qsort(seq, left, i-1)
  qsort(seq, i+1, right)
  
seq = [3, 8, 14, 12, 90, 1, 4, 29, 43 , 2, 10, 6, 37, 78, 50, 18]
qsort(seq, 0, len(seq)-1)
print(seq)