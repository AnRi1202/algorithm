def WarshallFloyd(V, e_matrix):
  dist = e_matrix
  inf = float('inf')
  d_i_j_k = [[[inf] * V] * V]*V
  print(dist)
  for i in V:
    for j in V:
      for k in V:
        if (d_i_j_k[i][k] != inf and d_i_j_k[k][j] != inf):
          d_i_j_k = min