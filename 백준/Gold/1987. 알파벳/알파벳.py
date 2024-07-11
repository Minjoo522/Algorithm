import sys
input = sys.stdin.readline

# 방향 배열
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def DFS(r, c, visited):
    if (r, c, visited) in memo:
        return memo[(r, c, visited)]

    max_depth = 1  # 현재 칸 포함
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < R and 0 <= nc < C:
            char_idx = ord(board[nr][nc]) - ord('A')
            if not (visited & (1 << char_idx)):
                max_depth = max(max_depth, 1 + DFS(nr, nc, visited | (1 << char_idx)))

    memo[(r, c, visited)] = max_depth
    return max_depth

R, C = map(int, input().split())
board = [input().rstrip() for _ in range(R)]

# 메모이제이션을 위한 딕셔너리
memo = {}

visited = 1 << (ord(board[0][0]) - ord('A'))

result = DFS(0, 0, visited)
print(result)
