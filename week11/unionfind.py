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