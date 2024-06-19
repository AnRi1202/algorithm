def qsort(seq, left, right):
  if right <= left:
    return
  pivot = seq[right]
  j = left
  for i in range(left, right):
    if seq[i] < pivot:
      seq[i], seq[j] = seq[j], seq[i]
      j += 1
  seq[j], seq[right] = seq[right], seq[j]
  qsort(seq, left, j-1)
  qsort(seq, j+1, right)
  return seq
