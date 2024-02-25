import sys

input = sys.stdin.readline

n = int(input())

total = 1
cnt = 1
while n > total:
    total += 6 * cnt
    cnt += 1
print(cnt)