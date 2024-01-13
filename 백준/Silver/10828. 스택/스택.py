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
        try:
            print(stack.pop())
        except:
            print(-1)
        finally:
            continue
    if command[0] == 'size':
        print(len(stack))
        continue
    if command[0] == 'empty':
        print(1 if len(stack) == 0 else 0)
        continue
    if command[0] == 'top':
        try:
            print(stack[-1])
        except:
            print(-1)
        finally:
            continue