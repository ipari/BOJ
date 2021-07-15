import sys


N, M, V = map(int, sys.stdin.readline().split())

vs1 = [v for v in range(1, N + 1)]
es1 = []
for m in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    es1.append(sorted([v1, v2]))

# BFS 에서 사용
vs2 = vs1.copy()
es2 = es1.copy()


def get_connected_vs(v1, vs, es):
    # 간선의 목록에서 v와 연결된 v들을 찾는다.
    connected_vs = []
    for e in es:
        if v1 not in e:
            continue
        i = 1 if e.index(v1) == 0 else 0
        v2 = e[i]
        if v2 not in vs:
            connected_vs.append(e[i])
    return sorted(connected_vs)


# DFS
dfs = []
dfs_stack = [V]

while dfs_stack:
    v1 = dfs_stack[-1]
    if v1 not in dfs:
        dfs.append(v1)

    connected_vs = get_connected_vs(v1, dfs, es1)
    if not connected_vs:
        dfs_stack.pop()
        continue

    v2 = connected_vs[0]
    es1.remove(sorted([v1, v2]))
    dfs_stack.append(v2)

print(' '.join(map(str, dfs)))


# BFS
bfs = []
bfs_queue = [V]

while bfs_queue:
    v1 = bfs_queue.pop(0)
    bfs.append(v1)
    connected_vs = get_connected_vs(v1, bfs, es2)
    if not connected_vs:
        continue
    for v2 in connected_vs:
        es2.remove(sorted([v1, v2]))
        if v2 not in bfs_queue:
            bfs_queue.append(v2)

print(' '.join(map(str, bfs)))
