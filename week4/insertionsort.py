def insertionsort(seq):
    for i in range(1, len(seq)):
        j = i - 1
        tmp = seq[i]
        # seq[j] > tmp の部分は、比較を行っている
        # j > -1 の部分は、リストの先頭を越えないようにするため
        while j >= 0 and seq[j] > tmp:
            seq[j + 1] = seq[j]
            j -= 1
        seq[j + 1] = tmp
    return seq

# 具体例
example_list = [3, 1, 4, 2, 5]
sorted_list = insertionsort(example_list)
print("ソート後のリスト:", sorted_list)
