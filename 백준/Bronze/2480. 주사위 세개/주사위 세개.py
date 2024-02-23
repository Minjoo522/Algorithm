import sys
from collections import defaultdict

input = sys.stdin.readline

nums = list(map(int, input().split()))

counts = defaultdict(int)

for num in nums:
    counts[num] += 1

max_value = 0
max_key = ""

for key, value in counts.items():
    if value > max_value:
        max_value = value
        max_key = key

if max_value == 3:
    print(f"{10000 + int(max_key) * 1000}")
elif max_value == 2:
    print(f"{1000 + int(max_key) * 100}")
else:
    print(f"{max(nums) * 100}")
