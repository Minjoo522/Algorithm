import sys

input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def DFS(r, c, visited):
    global result
    result = max(result, len(visited))

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in visited:
            visited.add(board[nr][nc])
            DFS(nr, nc, visited)
            visited.remove(board[nr][nc])


R, C = map(int, input().split())
board = [input().rstrip() for _ in range(R)]

visited = set()
visited.add(board[0][0])
result = 0

DFS(0, 0, visited)
print(result)