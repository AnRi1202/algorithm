import sys

def main(lines):
  class Queue:
    def __init__(self, size):
      self.queue = [None]*size
      self.head = 0
      self.tail = 0
      
    def enqueue(self,a:int):
      if self.tail < len(self.queue):
        self.queue[self.tail] = a
        self.tail += 1
        print(self.queue)
      else:
        print("full")
    
    def dequeue(self):
      if self.head < self.tail:
        tmp = self.queue[self.head]
        self.queue[self.head] = None
        self.head += 1
        return tmp
      else:
        print("empty")   

    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    Q = int(lines[0])
    # x = Queue(Q)
    # y = Queue(Q)

    count = 0
    for i in range(Q):
        if len(lines[i+1].split()) >= 2:
            count += 1
            a, b = map(int, lines[i+1].split()) 
            if(count ==  1):
                x=[b]
            else:
                x.append(b)
                #小さい順にxを並べる sortを使わずに
                for j in range(count-1,0,-1):
                    if x[j] < x[j-1]:
                        tmp = x[j]
                        x[j] = x[j-1]
                        x[j-1] = tmp
                    else:
                        break
        else:
            sum = 0

            middle = int(count/2)
            middle_number =x[middle-1]
            for j in range(count):
                print(x[j] )
            print("middle =",middle,"middle_number=",middle_number)    
            for j in range(middle):
                sum += middle_number -x[j]
                sum += x[count-middle] - middle_number
            print(sum)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
