import sys

input = sys.stdin.readline

N, M = map(int, input().split())
snacks = list(map(int, input().split()))

start, end = 1, max(snacks)

answer = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for snack in snacks:
        cnt += snack // mid

    # 과자가 N명 이상 -> 더 긴 길이도 가능?
    if cnt >= N:
        answer = mid
        start = mid + 1
    # 과자 부족 -> 길이 줄이기
    else:
        end = mid - 1

print(answer)