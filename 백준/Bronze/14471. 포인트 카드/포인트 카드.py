import sys

input = sys.stdin.readline

N, M = map(int, input().split())
costs = []

for _ in range(M):
    i, j = map(int, input().split())
    if N - i > 0:
        costs.append(N - i)
    else:
        costs.append(0)

costs.sort()

print(sum(costs[:M - 1]))