def insertionsort(seq):
  for i in range(1, len(seq)):
    j = i-1
    tmp = seq[i]
    while seq[j] > tmp and j > -1:
      seq[j+1] = seq[j]
      j -=1
    seq[j+1] = tmp
  return seq

#O(n^2)