import sys

input = sys.stdin.readline

N = int(input())

if N == 1:
    print(1)
else:
    while N % 2 == 0:
        N //= 2

    if N == 1:
        print(1)
    else:
        print(0)