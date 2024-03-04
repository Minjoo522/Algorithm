import sys
from collections import deque

input = sys.stdin.readline

my_queue = deque()

for _ in range(int(input())):
    command = list(input().rstrip().split())
    if command[0] == "push":
        my_queue.append(int(command[1]))
    elif command[0] == "pop":
        if my_queue:
            print(my_queue.popleft())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(my_queue))
    elif command[0] == "empty":
        if my_queue:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if my_queue:
            print(my_queue[0])
        else:
            print(-1)
    elif command[0] == "back":
        if my_queue:
            print(my_queue[-1])
        else:
            print(-1)
