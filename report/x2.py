
import sys

# Calculate difference of p1 from p2
def diff_pair(p1, p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]
    return (a, b)

# 1,2,3が反時計なら正　時計なら負
def signed_area(p1, p2, p3):
    v1 = diff_pair(p2, p1)
    v2 = diff_pair(p3, p1)
    return v1[0] * v2[1] - v1[1] * v2[0]  # Calculate area as z-component of v1 x v2

# Partition for quick sort
def partition(node, l, r, p_minx):
    pivot = node[r]
    i = l - 1
    for j in range(l, r):
        # Compare func: signed_area ~ Declination from p with min x
        # signed_area < 0 => clockwise
        if signed_area(p_minx, node[j], pivot) >= 0:
            i += 1
            node[i], node[j] = node[j], node[i]
    node[i + 1], node[r] = node[r], node[i + 1]
    return i + 1

# Sort points counter-clockwise
def qsort_c_clockwise(node, l, r, p_minx):
    if l < r:
        pivot = partition(node, l, r, p_minx)
        qsort_c_clockwise(node, l, pivot - 1, p_minx)
        qsort_c_clockwise(node, pivot + 1, r, p_minx)

# Remove concave points
def remove_concave(node):
    max_step = len(node) ** 3  # All combinations of triangle = nC3
    step = 0
    i = 0
    while i < len(node) - 2 and step < max_step:
        area = signed_area(node[i + 1], node[i + 2], node[i])
        # area < 0 => line graph of these points dents
        # => remove concave point
        # => check for new set again
        if area <= 0:
            node.pop(i + 1)
            i = 0
        else:
            i += 1
        step += 1

def graham_scan(node):
    # Iterator of the node with min x components
    itr_minx = min(node, key=lambda p: p[0])
    # Move min element to head
    node.remove(itr_minx)
    node.insert(0, itr_minx)
    qsort_c_clockwise(node, 0, len(node) - 1, node[0])
    remove_concave(node)

def main():
    # Input
    N = int(input("# of points = "))
    if N < 3:
        print("N >= 3")
        sys.exit(1)
    
    node = []
    for _ in range(N):
        x, y = map(int, input().split())
        node.append((x, y))
    
    graham_scan(node)
    
    # Output
    print("nodes of the convex hull:")
    for p in node:
        print(p[0], p[1])

if __name__ == "__main__":
    main()