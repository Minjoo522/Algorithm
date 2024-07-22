import sys

input = sys.stdin.readline

N, M = map(int, input().split())
times = [int(input()) for _ in range(N)]

start = 0
end = min(times) * M
result = 0

while start <= end:
    mid = (start + end) // 2

    cnt = sum(mid // time for time in times)  # 각 심사대에서 시간 안에 받을 수 있는 최대 인원

    if cnt >= M:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)
