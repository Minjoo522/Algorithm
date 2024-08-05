import sys

input = sys.stdin.readline

N = int(input())
M = int(input())  # 고정석 개수
vip_seats = [int(input()) for _ in range(M)]

dp = [0] * (N + 1)
dp[0], dp[1] = 1, 1

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

result = 1
previous_vip = 0

for vip in vip_seats:
    length = vip - previous_vip - 1  # vip 좌석 전까지만 not 고정
    result *= dp[length]
    previous_vip = vip

# 마지막 구간 처리
length = N - previous_vip
result *= dp[length]

print(result)
