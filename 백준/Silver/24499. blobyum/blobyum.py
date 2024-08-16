import sys

input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))
nums = nums + nums[:K]

current = sum(nums[:K])
result = sum(nums[:K])

for i in range(K, len(nums)):
    current += nums[i] - nums[i - K]
    result = max(result, current)

print(result)
