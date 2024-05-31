import sys

input = sys.stdin.readline

N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0
current_end = 0

for start, end in meetings:
    if start >= current_end:
        current_end = end
        cnt += 1

print(cnt)
