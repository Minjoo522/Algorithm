import sys
input = sys.stdin.readline

from collections import deque

queue = deque()

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'push':
        queue.append(command[1])
        continue
    if command[0] == 'pop':
        print(queue.popleft() if queue else -1)
        continue
    if command[0] == 'size':
        print(len(queue))
        continue
    if command[0] == 'empty':
        print(0 if queue else 1)
        continue
    if command[0] == 'front':
        print(queue[0] if queue else -1)
        continue
    if command[0] == 'back':
        print(queue[-1] if queue else -1)
        continue