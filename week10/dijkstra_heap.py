import heapq

edges_list = [
    [[1, 5], [2, 4]], # ノードA
    [[0, 5], [3, 3], [5, 9]], # ノードB
    [[0, 4], [3, 2], [4, 3]], # ノードC
    [[1, 3], [2, 2], [5, 1], [6, 7]], # ノードD
    [[2, 3], [6, 8]], # ノードE
    [[1, 9], [3, 1], [6, 2], [7, 5]], # ノードF
    [[3, 7], [4, 8], [5, 2], [7, 2]], # ノードG
    [[5, 5], [6, 2]] # ノードH
]

def dijkstra_heap(V, e_list):
    inf = float('inf')
    dist = [inf] * V
    dist[0] = 0
    node_heap = []
    heapq.heappush(node_heap, (0, 0))  # (distance, node)
    
    while node_heap:
        cur_dist, cur_node = heapq.heappop(node_heap)
        
        if cur_dist > dist[cur_node]:
            continue

        for neighbor, weight in e_list[cur_node]:
            distance = cur_dist + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(node_heap, (distance, neighbor))
    
    return dist

print(dijkstra_heap(8, edges_list))
