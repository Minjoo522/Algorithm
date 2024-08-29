import sys

input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    n = int(input())
    base = [i for i in range(n + 1)]
    acc = [0] * (n + 1)
    acc[1] = base[1]

    for i in range(k):
        for j in range(2, n + 1):
            acc[j] = acc[j - 1] + base[j]
        base = acc

    print(acc[n])