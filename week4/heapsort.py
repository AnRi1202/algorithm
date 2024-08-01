import heapq

def heapsort(seq):
  heap = []
  while seq:
    heapq.heappush(heap, seq.pop())
  while heap:
    seq.append(heapq.heappop(heap))
  return seq

seq = [3, 8, 14, 12, 90, 1, 4, 29, 43 , 2, 10, 6, 37, 78, 50, 18]
print(heapsort(seq))