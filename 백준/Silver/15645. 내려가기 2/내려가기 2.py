import sys

input = sys.stdin.readline


def max_min_score(N, board):
    max_dp = [[0] * 3 for row in board]
    min_dp = [[0] * 3 for row in board]

    for i in range(3):
        max_dp[0][i] = board[0][i]
        min_dp[0][i] = board[0][i]

    for i in range(1, N):
        for j in range(3):
            if j == 0:
                max_dp[i][j] = board[i][j] + max(max_dp[i - 1][j], max_dp[i - 1][j + 1])
                min_dp[i][j] = board[i][j] + min(min_dp[i - 1][j], min_dp[i - 1][j + 1])
            elif j == 1:
                max_dp[i][j] = board[i][j] + max(max_dp[i - 1][j], max_dp[i - 1][j + 1], max_dp[i - 1][j - 1])
                min_dp[i][j] = board[i][j] + min(min_dp[i - 1][j], min_dp[i - 1][j + 1], min_dp[i - 1][j - 1])
            elif j == 2:
                max_dp[i][j] = board[i][j] + max(max_dp[i - 1][j], max_dp[i - 1][j - 1])
                min_dp[i][j] = board[i][j] + min(min_dp[i - 1][j], min_dp[i - 1][j - 1])

    return max(max_dp[N - 1]), min(min_dp[N - 1])


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

print(*max_min_score(N, board))
