Q =3
K = 5
#リングバッファの作成
class Lingbuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [0]*size
        self.head = 0
        self.tail = 0
        self.count = 0

    def push(self, value):
        if self.count == self.size:
            return False
        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        self.count += 1
        return True

    def pop(self):
        if self.count == 0:
            return None
        value = self.buffer[self.head]
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return value

Lingbuffer = Lingbuffer(K)
