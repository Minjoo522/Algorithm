import sys

input = sys.stdin.readline

while True:
    a, b, c, d = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and d == 0:
        break

    result = 0
    while len({a, b, c, d}) != 1:
        na = abs(a - b)
        nb = abs(b - c)
        nc = abs(c - d)
        nd = abs(d - a)
        a = na
        b = nb
        c = nc
        d = nd
        result += 1

    print(result)
