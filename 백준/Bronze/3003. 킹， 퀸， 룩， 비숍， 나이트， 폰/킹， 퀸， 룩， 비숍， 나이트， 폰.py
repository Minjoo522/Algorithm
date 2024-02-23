import sys

input = sys.stdin.readline

chess = [1, 1, 2, 2, 2, 8]
donghyeok_chess = list(map(int, input().split()))
result = [0 for _ in range(len(chess))]

for i in range(len(chess)):
    result[i] = chess[i] - donghyeok_chess[i]

print(*result)
