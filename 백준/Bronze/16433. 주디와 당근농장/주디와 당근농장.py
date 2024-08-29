import sys

input = sys.stdin.readline

N, R, C = map(int, input().split())
farm = [['.'] * N for _ in range(N)]

dr = (1, -1, -1, 1)
dc = (-1, -1, 1, 1)

stack = [(R - 1, C - 1)]
visited = set(stack)

while stack:
    r, c = stack.pop()
    farm[r][c] = 'v'
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
            stack.append((nr, nc))
            visited.add((nr, nc))

for row in farm:
    print(''.join(row))