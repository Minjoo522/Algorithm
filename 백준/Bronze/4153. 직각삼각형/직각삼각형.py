import sys

input = sys.stdin.readline

while True:
    sides = list(map(int, input().split()))

    if sum(sides) == 0:
        break

    sides.sort()

    if sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2:
        print('right')
    else:
        print('wrong')