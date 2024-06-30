import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations

def circumcircle(p1, p2, p3):
    """ 三角形の外接円の中心と半径を計算する """
    ax, ay = p1
    bx, by = p2
    cx, cy = p3

    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    if d == 0:
        return None, float('inf')

    ux = ((ax**2 + ay**2) * (by - cy) + (bx**2 + by**2) * (cy - ay) + (cx**2 + cy**2) * (ay - by)) / d
    uy = ((ax**2 + ay**2) * (cx - bx) + (bx**2 + by**2) * (ax - cx) + (cx**2 + cy**2) * (bx - ax)) / d
    r = np.sqrt((ax - ux)**2 + (ay - uy)**2)

    return (ux, uy), r

def is_point_in_circumcircle(p, circumcenter, radius):
    return np.linalg.norm(np.array(p) - np.array(circumcenter)) < radius

def bowyer_watson(points):
    # ステップ1: 巨大三角形を追加
    super_triangle = [(-1, -1), (2, -1), (0.5, 2)]
    triangles = [super_triangle]

    for p in points:
        bad_triangles = []
        for tri in triangles:
            circumcenter, radius = circumcircle(*tri)
            if circumcenter is None:
                continue
            if is_point_in_circumcircle(p, circumcenter, radius):
                bad_triangles.append(tri)

        polygon = []
        for tri in bad_triangles:
            for edge in combinations(tri, 2):
                shared = False
                for other_tri in bad_triangles:
                    if tri != other_tri and set(edge).issubset(set(other_tri)):
                        shared = True
                        break
                if not shared:
                    polygon.append(edge)

        for tri in bad_triangles:
            triangles.remove(tri)

        for edge in polygon:
            new_tri = edge + (tuple(p),)
            triangles.append(new_tri)

    triangles = [tri for tri in triangles if not any(vertex in super_triangle for vertex in tri)]

    return triangles

# 点の生成
points = np.random.rand(100, 2)

# ドロネー三角分割の計算
triangles = bowyer_watson(points)

# プロット
plt.figure(figsize=(8, 6))
for tri in triangles:
    tri_points = np.array(tri)
    plt.fill(tri_points[:, 0], tri_points[:, 1], edgecolor='black', fill=False)
plt.plot(points[:, 0], points[:, 1], 'o')
plt.title('Delaunay Triangulation (Bowyer-Watson Algorithm)')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()