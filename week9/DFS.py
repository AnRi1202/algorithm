edges_list = [
[1, 2],#ノードA
[0, 3, 5],#ノードB
[0, 3, 4],#ノードC
[1, 2, 5],#ノードD
[2, 6],#ノードE
[1, 3, 7],#ノードF
[4],#ノードG
[5]]#ノードH

import sys
import resource
from collections import deque
sys.setrecursionlimit(1000000)
resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))

def dfs(edges, start, end, visited):
    if start == end:
        return True
    visited[start] = 1
    for n in edges[start]:
        if visited[n] == 0:
            if dfs(edges, n, end, visited):
                return True
    return False

def main(lines):
    N, M, S, T = map(int,lines[0].split())
    edges_list =[[] for i in range(N + 1)]
    for line in lines[1:]:
        u, v = map(int, line.split())
        edges_list[u].append(v)
        edges_list[v].append(u) 
    visited = [0] * (N + 1)

    if dfs(edges_list, S ,T , visited):
        print("Yes")
    else:
        print("No")    
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
