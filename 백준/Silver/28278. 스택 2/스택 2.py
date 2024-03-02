import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
stack = deque()

for _ in range(N):
    line = input().rstrip()
    command = int(line[0])
    if command == 1:
        stack.append(int(line[2:]))
    elif command == 2:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command == 3:
        print(len(stack))
    elif command == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack) - 1])
