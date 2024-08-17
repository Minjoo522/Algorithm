import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a = int(input())
    while a > 1 and a % 2 == 0:
        a //= 2

    if a == 1:
        print(1)
    else:
        print(0)