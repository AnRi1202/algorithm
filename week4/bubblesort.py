def bubblesort(seq):
  size = len(seq)
  for i in range(size):
    for j in range(size -1, i, -1):
      if seq[j] < seq[j -1]:
        seq[j] , seq[j -1] = seq[j-1], seq[j]
  return seq
seq = [3, 8, 14, 12, 90, 1, 4, 29, 43 , 2, 10, 6, 37, 78, 50, 18]

print(bubblesort(seq))