import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
B = [list(input().rstrip()) for _ in range(N)]

drs, dcs = [0, 0, 1, -1], [-1, 1, 0, 0]
visited = set()

def BFS(r, c, target_color, change_color):
    queue = deque([(r, c)])
    visited.add((r, c))
    A[r][c] = change_color

    while queue:
        curr_r, curr_c = queue.popleft()

        for dr, dc in zip(drs, dcs):
            nr, nc = curr_r + dr, curr_c + dc
            if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visited and A[nr][nc] == target_color:
                A[nr][nc] = change_color
                visited.add((nr, nc))
                queue.append((nr, nc))

for r in range(N):
    for c in range(M):
        if (r, c) not in visited and A[r][c] != B[r][c]:
            BFS(r, c, A[r][c], B[r][c])

for r in range(N):
    for c in range(M):
        if A[r][c] != B[r][c]:
            print('NO')
            sys.exit()

print('YES')