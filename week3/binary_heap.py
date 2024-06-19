import sys

def main(lines):
    class binary_heap:
        def __init__(self,size):
            self.size = size + 1
            self.inf = 0
            self.array =[self.inf] * self.size
            self.last = 0

    
        def add(self, value:int):
            if self.last == self.size:
                print("Heap is full")
                return
            else:
                self.last += 1
                self.array[self.last] = value
                self.check_after_add(self.last)


        def remove(self):
            if self.last == 0:
                print("Heap is empty")
                return
            else:
                removed = self.array[1]
                self.array[1] = self.array[self.last]
                self.last -= 1
                self.check_after_remove(1)
                print(removed)


        def check_after_add(self, i):
            if i == 1 or( self.array[i] <= self.array[i//2]):
                return
            else:
                parent = i // 2
                if self.array[parent] < self.array[i]:
                    self.array[parent], self.array[i] = self.array[i], self.array[parent]
                    self.check_after_add(parent)


        def check_after_remove(self, i):
            left = 2 * i
            right = 2 * i + 1
            parent = i
            if (self.array[parent] >= self.array[left] and left >= self.last) or(left >= self.last):
              return
            else:
              if(self.array[left] >= self.array[right]):
                self.array[parent], self.array[left] = self.array[left], self.array[parent]
                self.check_after_remove(left)
              else:
                self.array[parent], self.array[right] = self.array[right], self.array[parent]
                self.check_after_remove(right)
                
              
                
              
    Q = int(lines[0])

    Binary_heap = binary_heap(Q)
    for i in range(Q):
        if len(lines[i+1].split()) >= 2:
            a, b = map(int, lines[i+1].split()) 
        else:
            a = int(lines[i+1])

        
        if a == 1:
            Binary_heap.add(b)
        if a== 2:
            Binary_heap.remove()  


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

        