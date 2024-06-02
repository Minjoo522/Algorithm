import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, 1, -1, -1, 1, -1, 1]

N = int(input())

board = [input().rstrip() for _ in range(N)]
user = [input().rstrip() for _ in range(N)]

ans = [['.'] * N for _ in range(N)]
found = False

for r in range(N):
    for c in range(N):
        if user[r][c] == 'x':
            cnt = 0
            for d in range(8):
                nr, nc = r + dr[d], c + dc[d]

                if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == '*':
                    cnt += 1
            ans[r][c] = str(cnt)  # join 하기 위해서 string으로 저장해주어야 함

            if board[r][c] == '*':
                found = True

if found:
    for r in range(N):
        for c in range(N):
            if board[r][c] == '*':
                ans[r][c] = '*'

for line in ans:
    print(''.join(line))