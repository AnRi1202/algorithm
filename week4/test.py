import sys

def main(lines):

    Q = int(lines[0])
    num = {}  # 辞書を使用する
    for i in range(Q):
        a, b = map(int, lines[i+1].split()) 
        b_surplus = b % Q

        if a == 0:
            if b_surplus not in num:
                num[b_surplus] = b
            else:
                print("error")
            
        elif a == 1:
            if b_surplus in num and num[b_surplus] == b:
                print("found")
                del num[b_surplus]
            else:
                print("not found")
                
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
