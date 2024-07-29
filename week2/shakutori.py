N = input()
m = input()
sequence = [0]*N
sum_max = 0
sum_index = 0

##### naive shakutori O(Nm)
for i in range (N-m):
  tmp = 0
  for j in range(m-1):
    tmp += sequence[i+j]
    if tmp > sum_max:
      sum_max = tmp
      sum_index = i+j
      
####### better shakutori O(N)
tmp = sum(sequence[0:m-1])
max = tmp
m_index = 0

for i in range(N-m-1):
  tmp = tmp - sequence[i] + sequence[m+i]
  if tmp > max:
    max = tmp
    m_index = i
    
#### 尺取り法はn(n+1)/2のものをn回で終わらせる


    
