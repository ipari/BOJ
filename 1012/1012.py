import sys


def calc_worm(baechoos):
    # 인접 리스트 생성
    adj_baechoos = {}
    for b1 in baechoos:
        adj_bs = []
        for b2 in baechoos:
            if (b1[0] == b2[0] and abs(b1[1] - b2[1]) == 1) or (b1[1] == b2[1] and abs(b1[0] - b2[0]) == 1):
                adj_bs.append(b2)
        adj_baechoos[b1] = adj_bs

    # 방문한 배추 초기화
    visited_baechoos = {}
    for b in baechoos:
        visited_baechoos[b] = False

    # 배추 BFS 탐색
    worm = 0
    while baechoos:
        worm += 1
        queue = [baechoos[0]]

        while queue:
            b1 = queue.pop(0)
            if visited_baechoos[b1]:
                continue

            visited_baechoos[b1] = True
            baechoos.remove(b1)
            queue += adj_baechoos[b1]

    return worm


T = int(sys.stdin.readline())
for t in range(T):
    M, N, K = tuple(map(int, sys.stdin.readline().split()))
    baechoos = []
    for _ in range(1, K + 1):
        baechoos.append(tuple(map(int, sys.stdin.readline().split())))
    print(calc_worm(baechoos))
