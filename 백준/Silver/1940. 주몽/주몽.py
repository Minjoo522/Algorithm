import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
materials = list(map(int, input().split()))

materials.sort()

left = 0
right = N - 1
cnt = 0

while left < right:
    current_sum = materials[left] + materials[right]

    if current_sum == M:
        cnt += 1
        left += 1
        right -= 1
    elif current_sum < M:
        left += 1
    elif current_sum > M:
        right -= 1

print(cnt)