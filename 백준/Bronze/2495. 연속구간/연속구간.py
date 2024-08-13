import sys

input = sys.stdin.readline

for _ in range(3):
    nums = input().rstrip()

    max_cnt = current_cnt = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            current_cnt += 1
        else:
            current_cnt = 1
        max_cnt = max(max_cnt, current_cnt)

    print(max_cnt)