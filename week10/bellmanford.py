edges_list2 = [[0, 1, 5], [0, 2, 4], [1, 0, 5], [1, 3, 9], [1, 5, 9],
               [2, 0, 4], [2, 3, 2], [2, 4, 3], [3, 1, 9], [3, 2, 2], 
               [3, 5, 1], [3, 6, 7], [4, 2, 3], [4, 6, 8], [5, 1, 9], 
               [5, 3, 1], [5, 6, 2], [5, 7, 5], [6, 3, 7], [6, 4, 8], 
               [6, 5, 2], [6, 7, 2], [7, 5, 5], [7, 6, 2]]

def BellmanFord(V, edges_list):
    inf = float('inf')
    dist = [inf] * V
    dist[0] = 0

    for i in range(V - 1):
        for e in edges_list:
            u, v, w = e
            if dist[u] != inf and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # 負の閉路の検知
    for e in edges_list:
        u, v, w = e
        if dist[u] != inf and dist[u] + w < dist[v]:
            return -1  # 負の閉路が検出された場合

    return dist

V = 8  # ノード数
print(BellmanFord(V, edges_list2))
