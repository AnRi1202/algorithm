V = 5
E = 6
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 4], [3, 4]]

from collections import deque
def KahnTopo(V, E, edges):
  indeg = [0]*V # ⼊次数を格納する配列
# 出⼒辺を保持する配列
  outedge = [[] for _ in range (V)]
  for v_from, v_to in edges:
    indeg[v_to] += 1
    outedge[v_from].append(v_to)
    sorted_g = list(v for v in range(V) if indeg[v] == 0)
    
    deq = deque(sorted_g)
    
  while deq:
    v = deq.popleft()
    for u in outedge[v]:
      E -= 1
      indeg[u] -= 1
      if indeg[u] == 0:
        deq.append(u)
        sorted_g.append(u)
        
  if E !=0:
    return None
    
  return sorted_g
  
print(KahnTopo(V, E, edges))
