import sys

input = sys.stdin.readline

N, M = map(int, input().split())
weapons = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
dp[0] = weapons[0]

for i in range(1, N):
    min1 = 987654321
    min2 = 987654321
    min_index = -1

    for j in range(M):
        if dp[i - 1][j] < min1:
            min2 = min1
            min1 = dp[i - 1][j]
            min_index = j
        elif dp[i - 1][j] < min2:
            min2 = dp[i - 1][j]

    for j in range(M):
        if j == min_index:
            dp[i][j] = min2 + weapons[i][j]
        else:
            dp[i][j] = min1 + weapons[i][j]

print(min(dp[N - 1]))