import sys

N, M = map(int, sys.stdin.readline().split())
tree_heights = [int(x) for x in sys.stdin.readline().split()]

min_h = 0
max_h = max(tree_heights)

while(min_h <= max_h):
    mid = (min_h + max_h) // 2
    m = sum(h - mid for h in tree_heights if h > mid)
    if m >= M:
        min_h = mid + 1
    else:
        max_h = mid - 1

print(max_h)
