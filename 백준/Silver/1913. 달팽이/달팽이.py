import sys

input = sys.stdin.readline

# 하, 우, 상, 좌
dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)


def find_value(snail, value):
    for r in range(len(snail)):
        for c in range(len(snail)):
            if snail[r][c] == value:
                return r + 1, c + 1


N = int(input())
find = int(input())

snail = [[0] * N for _ in range(N)]
r, c, d = 0, 0, 0

for num in range(N ** 2, 0, -1):
    snail[r][c] = num

    nr, nc = r + dr[d], c + dc[d]

    if nr < 0 or nr >= N or nc < 0 or nc >= N or snail[nr][nc] != 0:
        d = (d + 1) % 4
        nr, nc = r + dr[d], c + dc[d]

    r, c = nr, nc

for ans in snail:
    print(*ans)

print(*find_value(snail, find))
