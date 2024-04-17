N, M = map(int, input().split())
List = list(map(int, input().split()))

max = 0
index = 0
tmp = sum(List[0:M])
for i in range(N-M):
  print(i)
  tmp = tmp - List[i] + List[i+M]
  if tmp > max:
    max = tmp
    print(max, i+1)
    index = i+2

    
    
print(max, index)