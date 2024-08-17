import sys

input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    if all(num == 0 for num in nums):
        break

    result = 0
    while len(set(nums)) != 1:
        nums = [abs(nums[i] - nums[i - 1]) for i in range(4)]
        result += 1

    print(result)
   