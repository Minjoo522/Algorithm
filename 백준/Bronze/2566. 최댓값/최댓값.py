import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]

max_value = 0
max_index = [0, 0]

for x in range(9):
    for y in range(9):
        if board[x][y] >= max_value:
            max_value = board[x][y]
            max_index[0], max_index[1] = x + 1, y + 1

print(max_value)
print(*max_index)
