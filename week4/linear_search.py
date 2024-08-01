def linear_search(sequence, key):
  i = 0
  
  while i < len(sequence):
    if (sequence[i] == key):
      return i
    i+= 1
  return -1
  
  
def linear_searhch2(sequence, key):
  i = 0
  sequence.append(key)
  while sequence[i] != key:
    i +=1
  if i == len(sequence) -1:
    return -1
  return i

#比較が一回分減る
