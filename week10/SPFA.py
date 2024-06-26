from collections import deque

edges_list = [
    [[1, 5], [2, 4]],  # ノードA
    [[0, 5], [3, 3], [5, 9]],  # ノードB
    [[0, 4], [3, 2], [4, 3]],  # ノードC
    [[1, 3], [2, 2], [5, 1], [6, 7]],  # ノードD
    [[2, 3], [6, 8]],  # ノードE
    [[1, 9], [3, 1], [6, 2], [7, 5]],  # ノードF
    [[3, 7], [4, 8], [5, 2], [7, 2]],  # ノードG
    [[5, 5], [6, 2]]  # ノードH
]

def spfa(V, e_list):
    inf = float('inf')
    dist = [inf] * V
    dist[0] = 0

    node_to_check = deque()
    in_queue = [False] * V
    node_to_check.append(0)
    in_queue[0] = True
    count = 0

    while node_to_check:
        cur_node = node_to_check.popleft()
        in_queue[cur_node] = False

        for e in e_list[cur_node]:
            count += 1
            if dist[e[0]] > dist[cur_node] + e[1]:
                dist[e[0]] = dist[cur_node] + e[1]
                if not in_queue[e[0]]:
                    in_queue[e[0]] = True
                    node_to_check.append(e[0])

    print(dist)
    print(count)

spfa(8, edges_list)
