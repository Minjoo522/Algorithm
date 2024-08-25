import sys

input = sys.stdin.readline

N, M = map(int, input().split())
holes = list(map(int, input().split()))

sum = 0
left, right = 0, 0
result = 0

while right < N:
    if sum <= M:
        sum += holes[right]
        if right < N:
            right += 1
    else:
        sum -= holes[left]
        left += 1
    if sum <= M:
        result = max(result, sum)

print(result)
