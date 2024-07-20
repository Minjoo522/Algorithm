import sys

input = sys.stdin.readline


def dijkstra(start, end):
    dist = [987654321] * (N + 1)
    dist[start] = 0
    visited = [False] * (N + 1)

    for _ in range(1, N + 1):
        min_idx = -1
        min_value = 987654321

        for i in range(1, N + 1):  # dist 배열에서 visited 안 된 애들 중 가장 작은 노드 찾기
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]  # 갱신

        if min_idx == -1:
            break

        visited[min_idx] = True

        for i in range(1, N + 1):
            if not visited[i] and dist[i] > adj[min_idx][i] + dist[min_idx]:
                dist[i] = adj[min_idx][i] + dist[min_idx]

    return dist[end]


N = int(input())
M = int(input())
adj = [[987654321] * (N + 1) for _ in range(N + 1)]

# 인접행렬 만들기
for _ in range(M):
    start, end, w = map(int, input().split())
    if w < adj[start][end]:
        adj[start][end] = w

start, end = map(int, input().split())

print(dijkstra(start, end))
