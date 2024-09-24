import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
M //= 7

# 유튜버들의 기록을 주별로 관리 [횟수, 시간]
youtubers = [defaultdict(lambda: [0, 0]) for _ in range(M)]

for _ in range(N):
    name, day, start, end = input().rstrip().split()

    week_num = (int(day) - 1) // 7  # 주 번호 계산

    # 시간 계산
    hour = int(end[:2]) - int(start[:2])
    minute = int(end[-2:]) - int(start[-2:])
    if minute < 0:
        hour -= 1
        minute = 60 + minute
    time = hour * 60 + minute

    youtubers[week_num][name][0] += 1
    youtubers[week_num][name][1] += time

valid_virtuals = set()

for week in range(M):
    for name, (cnt, time) in youtubers[week].items():
        if cnt >= 5 and time >= 3600:
            valid_virtuals.add(name)

final_virtuals = set()

for name in valid_virtuals:
    if all(youtubers[week][name][0] >= 5 and youtubers[week][name][1] >= 3600 for week in range(M)):
        final_virtuals.add(name)

if final_virtuals:
    for v in sorted(final_virtuals):
        print(v)
else:
    print(-1)