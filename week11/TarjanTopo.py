from collections import deque

# 関数 Tarjantopo はグラフのトポロジカルソートを行います
def Tarjantopo(V, edges):
    def check(v):
        if visited[v] == 1:
            # ノードが訪問中ならサイクルがあるため False を返す
            return False
        elif visited[v] == 0:
            visited[v] = 1  # ノードを訪問中とマーク
            for u in outedge[v]:
                if not check(u):
                    # 再帰的に訪問してサイクルがあるかチェック
                    return False
            visited[v] = 2  # ノードの訪問を完了とマーク
            sorted_g.appendleft(v)  # ソート結果にノードを追加
        return True

    visited = [0] * V  # 訪問状態を管理するリスト: 0 = 未訪問, 1 = 訪問中, 2 = 訪問完了
    outedge = [[] for _ in range(V)]  # グラフの隣接リストを初期化
    
    for e in edges:
        outedge[e[0]].append(e[1])  # エッジを隣接リストに追加

    sorted_g = deque()  # トポロジカルソート結果を格納するデック

    for i in range(V):
        if visited[i] == 0:  # 未訪問のノードから探索を開始
            if not check(i):
                return None  # サイクルがある場合は None を返す

    return list(sorted_g)  # デックをリストに変換して返す

# テストの実行
V = 5
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 4], [3, 4]]
print(Tarjantopo(V, edges))

      