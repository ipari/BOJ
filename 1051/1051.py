import sys


N, M = map(int, sys.stdin.readline().split())
RECT = []
for _ in range(N):
    RECT.append(sys.stdin.readline())


def has_valid_rect(l):
    for y in range(N - l + 1):
        for x in range(M - l + 1):
            d = l - 1
            if RECT[y][x] == RECT[y + d][x] == RECT[y][x + d] == RECT[y + d][x + d]:
                return True


max_l = min(N, M)
for l in range(max_l, 0, -1):
    if has_valid_rect(l):
        print(l ** 2)
        break
