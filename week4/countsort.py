def countsort(seq, max_value):
  count = [0] * (max_value + 1)
  sorted =[]
  
  for i in range(len(seq)):
    count[seq[i]] += 1
  for i in range(len(count)):
    for j in range(count[i]):
      sorted.append(i)
  return sorted

seq = [3, 8, 14, 12, 90, 1, 4, 29, 43 , 2, 10, 6, 37, 78, 50, 18]

print(countsort(seq, 90))