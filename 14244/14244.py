import sys


N, M = map(int, sys.stdin.readline().split())

# 0과 1이 연결된 트리로 초기화
n = 2
m = 2
edges = [[0, 1]]
leaf_nodes = [0, 1]
non_leaf_nodes = []

# 리프 노드의 수 m은 non-리프 노드에 새 노드를 연결할 때 증가한다.
for x in range(2, N):
    # m < M이면 non-리프노드에 붙힌다.
    if m < M and non_leaf_nodes:
        y = non_leaf_nodes[-1]
        m += 1
    # m = M 이거나, non-리프노드가 없으면,
    else:
        y = leaf_nodes.pop()
        non_leaf_nodes.append(y)
        leaf_nodes.append(x)
    edges.append([y, x])
    n += 1

for edge in edges:
    print(' '.join(map(str, edge)))
