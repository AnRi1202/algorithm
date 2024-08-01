edges_list = [
[1, 2],#ノードA
[0, 3, 5],#ノードB
[0, 3, 4],#ノードC
[1, 2, 5],#ノードD
[2, 6],#ノードE
[1, 3, 7],#ノードF
[4],#ノードG
[5]]#ノードH

V = len(edges_list)

from collections import deque
n_name =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def bfs(edges, start, end):
  waiting = deque()
  
  done = [0]*V
  done[start] =2
  for n in edges[start]:
    done[n] =1
    waiting.append(n)
  while len(waiting):
    cur_node = waiting.popleft()
    if done[cur_node] != 2:
      done[cur_node] = 2
      print('Moved to {}'.format(n_name[cur_node]))
      if(end == cur_node): 
        print('=FOUND!=')
        return
      for n in edges[cur_node]:
        if done[n] == 0:
          done[n] = 1
          waiting.append(n)
        
bfs(edges_list, 0, 6)  