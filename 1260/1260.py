import sys


N, M, V = map(int, sys.stdin.readline().split())

# 인접 리스트를 먼저 만든다.
adj_list = [[] for _ in range(N + 1)]
for m in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)
# 정점 번호가 작은 것을 먼저 추가하기 용이하게 인접 리스트를 미리 정렬한다.
adj_list = [sorted(vs) for vs in adj_list]


def search_graph(adj_list, start_v, mode='DFS'):
    search_order = []
    search_buffer = [start_v]
    # 방문한 정점인지 여부를 정점의 값으로 바로 확인할 수 있도록
    visited_vs = [False for i in range(N + 1)]

    while search_buffer:
        # DFS, BFS 여부에 따라 버퍼를 각각 스택과 큐로 사용
        i = -1 if mode == 'DFS' else 0
        v1 = search_buffer.pop(i)

        # 이미 방문한 정점이면 지나감
        if visited_vs[v1]:
            continue

        visited_vs[v1] = True
        search_order.append(v1)

        # 인접 리스트의 값을 미리 정렬해두었다.
        # DFS는 스택이므로 작은 값이 뒤로 가게 역순으로 버퍼에 추가하고,
        # BFS는 큐이므로 작은 값이 앞으로 가게 버퍼에 추가한다.
        s = -1 if mode == 'DFS' else 1
        search_buffer += [v2 for v2 in adj_list[v1][::s] if not visited_vs[v2]]

    print(' '.join(map(str, search_order)))


search_graph(adj_list, V, mode='DFS')
search_graph(adj_list, V, mode='BFS')
