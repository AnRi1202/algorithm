def mergesort(seq):
    if len(seq) <= 1:
        return seq

    # リストを2つに分割
    mid = len(seq) // 2
    left = mergesort(seq[:mid])
    right = mergesort(seq[mid:])

    merged = []
    cur_l = cur_r = 0

    # 両方のリストから小さい要素をmergedに追加
    while cur_l < len(left) and cur_r < len(right):
        if left[cur_l] <= right[cur_r]:
            merged.append(left[cur_l])
            cur_l += 1
        else:
            merged.append(right[cur_r])
            cur_r += 1

    # 残った要素をmergedに追加
    if cur_l < len(left):
        merged.extend(left[cur_l:])
    if cur_r < len(right):
        merged.extend(right[cur_r:])

    return merged

# テストの実行
print(mergesort([3, 6, 2, 8, 7, 5, 1, 4]))
