w_limit= 15
weight = [11, 2, 3, 4, 1, 5]
value = [15, 3, 1, 4, 2, 8]
note = [[-1 for _ in range(w_limit+1)] for _ in range(len(weight))]
def knapsack_rec(cur_i, cur_w):
  if cur_i < 0: return 0
  if note[cur_i][cur_w] > -1: return note[cur_i][cur_w]

  
  if cur_w < weight[cur_i]:
    note[cur_i][cur_w] = knapsack_rec(cur_i - 1, cur_w)
    return note[cur_i][cur_w]

print(knapsack_rec(5, 15))