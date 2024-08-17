import sys

input = sys.stdin.readline

N = int(input())
hands = [1, 2]

if N % 2 == 0:
    result = hands * (N // 2)
else:
    result = hands * (N // 2) + [3]

print(*result)