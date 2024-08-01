class Node:
  def __init__(self, value):
    self.data = value
    self.left = None
    self.right = None
  def print(self):
    print((str(self.left.data) if self.left != None else "") + "/" + str(self.data) + " /" + str(self.right.data) if self.right != None else "")
  
class BinarySearchTree:
  def __init__(self):
    self.root = None
  
  def createTree(self, array):
    for i in range(len(array)):
      self.insert(array[i])
  
  def insert(self, value):
    if not self.root:
      self.root = Node(value)
    else:
      self._insertRec(self.root, value)
  
  def _insertRec(self, node, value):
    if value < node.data:
      if node.left:
        self._insertRec(node.left, value)
      else:
        node.left = Node(value)
    else:
      if node.right:
        self._insertRec(node.right, value)
      else:
        node.right = Node(value)
  
  def search(self, value):
    node = self.root
    while node:
      node.print()
      if node.data == value:
        print("found")
        return
      elif value < node.data:
        print("go left")
        node = node.left
      else:
        print("go right")
        node = node.right
    print("not found")
    
  def delete(self, value):
    self.root = self._deleteRec(self.root, value)
    
  def _findSuccessor(self, node):
    while node.left:
      node = node.left
    return node
  def _deleteRec(self,node, value):
    if not node:
      return node
    if value < node.data:
      node.left = self._deleteRec(node.left, value)
    elif value > node.data:
      node.right = self._deleteRec(node.right, value)
    else:
      if not node.left:
        return node.right
      elif not node.right:
        return node.left
      else:
        sucNode = self._findSuccessor(node.right)
        node.data = sucNode.data
        node.right = self._deleteRec(node.right, sucNode.data)
    return node


a = BinarySearchTree()
a.createTree([5,3,7,2,4,6,8])
a.search(3)
a.delete(3)
a.search(3)
