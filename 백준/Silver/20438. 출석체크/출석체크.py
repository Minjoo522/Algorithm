import sys

input = sys.stdin.readline

N, K, Q, M = map(int, input().split())
students = [0] * (N + 3)
sleep_nums = set(map(int, input().split()))
receive_nums = list(map(int, input().split()))

for num in receive_nums:
    if num not in sleep_nums:
        for i in range(num, N + 3, num):
            if i not in sleep_nums:
                students[i] = 1

# 누적 합
prefix_sum = [0] * (N + 3)
for i in range(1, N + 3):
    prefix_sum[i] = prefix_sum[i - 1] + (1 if students[i] == 0 else 0)

results = []
for _ in range(M):
    S, E = map(int, input().split())
    result = prefix_sum[E] - prefix_sum[S - 1]
    results.append(result)

print(*results)
