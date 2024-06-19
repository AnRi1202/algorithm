import sys

def main(lines):

    Q = int(lines[0])
    num = [-1]*Q
    
    for i in range(Q):

        a, b = map(int, lines[i+1].split()) 

        
        if a == 0:
            b_surplus = b % Q
            j = 0

            while num[(b_surplus+j)%Q] != -1:

                j+1
                if(j ==Q):
                    print("error")
                    break
            
            if(j !=Q):
                num[(b_surplus+j)%Q]=b  

        if a== 1:
            j = 0
            b_surplus = b%Q
            print(num[b_surplus])
            while num[(b_surplus+j)%Q] != b or j <Q:
                j+1
                if(j ==Q):
                    print("not found")
                    break
            
            if(j !=Q):
                print("found")
                num[(b_surplus+j)%Q] = -1 

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

        