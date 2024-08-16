import sys

input = sys.stdin.readline

N, K = map(int, input().split())

dx = (0, 0, -2, 2)
dy = (-2, 2, 0, 0)

def BFS(pieces):
    cnt = 0
    visited = set(pieces)

    for x, y in pieces:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if (nx, ny) not in visited and 0 < nx <= N and 0 < ny <= N:
                visited.add((nx, ny))
                cnt += 1
    return cnt

pieces = [tuple(map(int, input().split())) for _ in range(K)]
print(BFS(pieces))