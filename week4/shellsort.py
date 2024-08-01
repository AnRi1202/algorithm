def shellsort(seq):
    h = 1
    # ギャップシーケンスを決定
    while h < len(seq) // 3:
        h = h * 3 + 1
    # ギャップのサイズを縮小しながらソート
    while h >= 1:
        for i in range(h, len(seq)):
            j = i
            while j >= h and seq[j - h] > seq[j]:
                seq[j], seq[j - h] = seq[j - h], seq[j]  # 交換
                j -= h
        h //= 3
    return seq

# テスト用のシーケンス
seq = [3, 8, 14, 12, 90, 1, 4, 29, 43, 2, 10, 6, 37, 78, 50, 18]

print(shellsort(seq))
