import sys

input = sys.stdin.readline

from collections import deque

stack = deque()

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'push':
        stack.append(int(command[1]))
        continue
    if command[0] == 'pop':
        print(stack.pop() if stack else -1)
        continue
    if command[0] == 'size':
        print(len(stack))
        continue
    if command[0] == 'empty':
        print(0 if stack else 1)
        continue
    if command[0] == 'top':
        print(stack[-1] if stack else -1)
        continue