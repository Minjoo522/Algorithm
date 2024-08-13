import sys

input = sys.stdin.readline

for _ in range(3):
    nums = input().rstrip()
    current = nums[0]
    current_cnt = 1
    max_cnt = 1
    for i in range(1, 8):
        if current == nums[i]:
            current_cnt += 1
            max_cnt = max(max_cnt, current_cnt)
        else:
            current = nums[i]
            current_cnt = 1
    print(max_cnt)