def binary_search(seq, key):
  #legtm, rightに左、右端を指定
  left = 0; right = len(seq) -1
  
  while right >= left:
    pivot = (left + right) //2
    if seq[pivot] == key:
      return pivot
    elif seq[pivot] < key:
      left = pivot + 1
    else: right = pivot -1
  return -1

  
seq = [1,3,4,6,7,8,10]
key = 4

print(binary_search(seq, key))