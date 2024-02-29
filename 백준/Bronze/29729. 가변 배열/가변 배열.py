import sys

input = sys.stdin.readline

S, N, M = map(int, input().split())
U = 0

for i in range(N + M):
    command = int(input())
    if command == 1:
        if S == U:
            S *= 2
        U += 1
    else:
        U -= 1

print(S)
