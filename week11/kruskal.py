class UnionFind:
  def __init__(self, n):
    self.parent = [i for i in range(n)]
    self.height = [0 for _ in range(n)] # 各⽊の⾼さ
      
  def get_root(self, i):
    if self.parent[i] == i:
      return i
    else:
      self.parent[i] = self.get_root(self.parent[i])
      return self.parent[i]
    
  def unite(self,i,j):
    root_i = self.get_root(i)
    root_j = self.get_root(j)
    if root_i != root_j:
      if self.height[root_i] < self.height[root_j]:
        self.parent[root_i] = root_j
      else:
        self.parent[root_j] = root_i
        if self.height[root_i] == self.height[root_j]:
          self.height[root_i] += 1
  
  def is_in_group(self,i,j):
    if self.get_root(i) == self.get_root(j):
      return True
    else:
      return False
    
    
def kruskal(V,e_list):
  e_cost_sorted = []
  for e in e_list:
    e_cost_sorted.append([e[2], e[0], e[1]])
  
  e_cost_sorted.sort()
  uf_tree = UnionFind(V)
  mst =[]
  for e in e_cost_sorted:
    if uf_tree.is_in_group(e[1], e[2]) == False:
      uf_tree.unite(e[1], e[2])
      mst.append([e[1],e[2]])
  
  mst.sort()
  print(mst)
      


edges_list = [[0, 1, 5], [0, 2, 4], [1, 0, 5], [1, 3, 3], [1, 5, 9],
[2, 0, 4], [2, 3, 2], [2, 4, 3], [3, 1, 3], [3, 2, 2], [3, 6, 7],
[3, 7, 5], [4, 2, 3], [4, 6, 8], [5, 1, 9], [6, 3, 7], [6, 4, 8],
[6, 7, 1], [7, 3, 5], [7, 6, 1]]
kruskal(8, edges_list)
  