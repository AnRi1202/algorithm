class MyHeap:
    def __init__(self, size):
        self.inf = 10**9
        self.size = size + 1  # ヒープのサイズ（+1は1ベースインデックス用）
        self.array = [self.inf] * self.size  # ヒープの配列を初期化
        self.last = 0  # 現在の要素数

    def add(self, value: int):
        if self.last + 1 < self.size:  # ヒープに空きがある場合
            self.last += 1
            self.array[self.last] = value
            self.check_after_add(self.last)
        else:
            print("Heap is full!")

    def remove(self):
        if self.last != 0:  # ヒープが空でない場合
            removed = self.array[1]
            self.array[1] = self.array[self.last]
            self.array[self.last] = self.inf
            self.last -= 1
            self.check_after_remove(1)
            return removed
        return None

    def check_after_add(self, i):
        if i < 2: return
        if self.array[i] < self.array[i // 2]:  # 親と比較して小さい場合
            self.array[i], self.array[i // 2] = self.array[i // 2], self.array[i]  # 親と交換
            self.check_after_add(i // 2)

    def check_after_remove(self, i):
        while i * 2 <= self.last:  # 子が存在する場合
            left = i * 2
            right = i * 2 + 1
            smaller_child = left
            
            if right <= self.last and self.array[right] < self.array[left]:
                smaller_child = right
            
            if self.array[i] > self.array[smaller_child]:
                self.array[i], self.array[smaller_child] = self.array[smaller_child], self.array[i]
                i = smaller_child
            else:
                break

# テストの実行
heap = MyHeap(5)
heap.add(5)
heap.add(3)
heap.add(7)
heap.add(1)
heap.add(9)

