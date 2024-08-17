import sys

input = sys.stdin.readline

N = int(input())
coordinate = [tuple(map(int, input().split())) for _ in range(N)]

# 마지막과 첫 번째 미리 더해주기
result = abs(coordinate[0][0] - coordinate[-1][0]) + abs(coordinate[0][1] - coordinate[-1][1])

for i in range(1, N):
    x1, y1 = coordinate[i - 1]
    x2, y2 = coordinate[i]
    result += abs(x1 - x2) + abs(y1 - y2)

print(result)