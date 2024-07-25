import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, end, weight):
    queue = deque()
    visited = [0] * (N + 1)
    visited[start] = True
    queue.append(start)

    while queue:
        x = queue.popleft()
        if x == end:
            return True
        for i in bridges[x]:
            if not visited[i[0]] and i[1] >= weight:
                visited[i[0]] = True
                queue.append(i[0])
    return False  # 가능한 섬을 다 바운 했는데 도착지에 도달하지 못했을 때


N, M = map(int, input().split())
bridges = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    bridges[a].append((b, c))
    bridges[b].append((a, c))

start, end = map(int, input().split())
low, high = 1, 1000000000
result = 0

while low <= high:
    mid = (low + high) // 2
    if bfs(start, end, mid):  # 점점 더 큰 값으로 갱신
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)
