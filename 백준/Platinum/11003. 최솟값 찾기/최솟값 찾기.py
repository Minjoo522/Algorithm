import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i], i))
    if mydeque[0][1] <= i - L:  # 윈도우 범위 넘어감 now index - L <= index
        mydeque.popleft()
    print(mydeque[0][0], end=' ')
