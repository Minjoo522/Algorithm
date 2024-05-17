import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
trains = [deque([0] * 20) for _ in range(N + 1)]

for i in range(M):
    command = list(map(int, input().split()))
    if command[0] == 1:
        train = command[1]
        seat = command[2] - 1
        trains[train][seat] = 1
    elif command[0] == 2:
        train = command[1]
        seat = command[2] - 1
        trains[train][seat] = 0
    elif command[0] == 3:
        train = command[1]
        trains[train].appendleft(0)
        trains[train].pop()
    elif command[0] == 4:
        train = command[1]
        trains[train].append(0)
        trains[train].popleft()

selected = set(tuple(train) for train in trains[1:])

print(len(selected))