capacity =[
[0, 10, 10, 0, 0, 0], # A->B: 10, A->C: 10
[0, 0, 0, 4, 8, 0], # B->D: 4, B->E: 8
[0, 0, 0, 7, 4, 0], # C->D: 7, C->E: 4
[0, 0, 0, 0, 0, 8], # D->F: 8
[0, 0, 0, 0, 0, 12], # E->F: 12
[0, 0, 0, 0, 0, 0] # Fから出ていくものなし．
]

def dfs_ff(s, e, flow):
  if s == e:
    return flow
  visited[s] = True
  for i in range(V):
    if visited[i]:continue
    if capacity[s][i] > 0:
      f = dfs_ff(i, e, min(flow, capacity[s][i]))
      if f > 0:
        capacity[s][i] -= f
        capacity[i][s] += f
        return f
  return 0

max_flow = 0
V = 6

while True:
  visited = [False for i in range(V)]
  f = dfs_ff(0, 5 ,10**9)
  if not f:break
  max_flow += f







print(max_flow)