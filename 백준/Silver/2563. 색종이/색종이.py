import sys
input = sys.stdin.readline

board = [[0] * 100 for _ in range(100)]

for _ in range(int(input())):
    X, Y = map(int, input().split())

    for x in range(X, X + 10):
        for y in range(Y, Y + 10):
            board[x][y] = 1

ans = sum(sum(line) for line in board)
print(ans)