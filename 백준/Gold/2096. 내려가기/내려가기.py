import sys

input = sys.stdin.readline

n = int(input())
pre = list(map(int, input().split()))
max_pre = pre[:]
min_pre = pre[:]

for _ in range(n - 1):
    aft = list(map(int, input().split()))

    max_pre = [
        aft[0] + max(max_pre[0], max_pre[1]),
        aft[1] + max(max_pre[0], max_pre[1], max_pre[2]),
        aft[2] + max(max_pre[1], max_pre[2])
    ]
    min_pre = [
        aft[0] + min(min_pre[0], min_pre[1]),
        aft[1] + min(min_pre[0], min_pre[1], min_pre[2]),
        aft[2] + min(min_pre[1], min_pre[2])
    ]

print(max(max_pre), min(min_pre))
