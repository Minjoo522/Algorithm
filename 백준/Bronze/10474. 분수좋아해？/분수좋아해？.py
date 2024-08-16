import sys

input = sys.stdin.readline

while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break

    print(f'{x // y} {x % y} / {y}')
