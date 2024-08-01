node_num = 4
F = 7
inf = float('inf')

graph = [
    {1: [3, 6], 2: [5, 2]}, # ノードA
    {0: [0, -6], 2: [0, -3], 3: [4, 3]}, # ノードB
    {0: [0, -2], 1: [7, 3], 3: [6, 9]}, # ノードC
    {1: [0, -3], 2: [0, -9]} # ノードD
]

def primal_dual(g, V, f):
    totalCost = 0
    cur_flow = 0

    while cur_flow < f:
        cost = [inf] * V
        cost[0] = 0
        route = [-1] * V
        flag = True

        while flag:
            flag = False
            for i in range(V):
                for dest_n, e in g[i].items():
                    if e[0] > 0 and cost[i] + e[1] < cost[dest_n]:
                        cost[dest_n] = cost[i] + e[1]
                        route[dest_n] = i
                        flag = True

        if cost[V-1] == inf:
            return -1  # 流量がFに達しない場合

        min_c = inf
        cur_n = V - 1
        while cur_n != -1:
            prev_n = route[cur_n]
            if prev_n == -1:
                break
            if g[prev_n][cur_n][0] < min_c:
                min_c = g[prev_n][cur_n][0]
            cur_n = prev_n

        if cur_flow + min_c > f:
            min_c = f - cur_flow

        totalCost += cost[V-1] * min_c
        cur_flow += min_c

        cur_n = V - 1
        while cur_n != -1:
            prev_n = route[cur_n]
            if prev_n == -1:
                break
            g[prev_n][cur_n][0] -= min_c
            g[cur_n][prev_n][0] += min_c
            cur_n = prev_n

    return totalCost

# プログラムの実行例
total_cost = primal_dual(graph, node_num, F)
print("最小コスト: ", total_cost)
