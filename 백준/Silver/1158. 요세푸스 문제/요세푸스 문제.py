import sys

input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())
people = deque(range(1, N + 1))
result = []

while people:
    people.rotate(-(K - 1))  # 왼쪽으로 K - 1번 회전
    result.append(str(people.popleft()))

print('<' + ', '.join(result) + '>')