import sys

input = sys.stdin.readline

keyboard = [list(input().rstrip()) for i in range(4)]
keys = input().rstrip()

dr = [0, 0, -1, 1, -1, 1, -1, 1]
dc = [-1, 1, 0, 0, 1, 1, -1, -1]

directions = set()
for r in range(4):
    for c in range(10):
        if keyboard[r][c] in keys:
            directions.add((r, c))

for r, c in directions:
    cnt = 0
    for i in range(8):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < 4 and 0 <= nc < 10 and (nr, nc) in directions:
            if keyboard[nr][nc] in keys:
                cnt += 1
            else:
                continue
    if cnt == 8:
        print(keyboard[r][c])
