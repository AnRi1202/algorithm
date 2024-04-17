Money , Level = map(int, input().split())
N = int(input())
for i in range(N):
  name, price, level = map(str, input().split())
  price = int(price)
  level = int(level)
  if Money >= price and Level >= level:
    print(name + " " + str(price))

    