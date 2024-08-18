import sys

input = sys.stdin.readline

for _ in range(int(input())):
    num = int(input())
    cnt = 0

    while num != 6174:
        digits = sorted(str(num).zfill(4))
        max_num = int(''.join(digits[::-1]))
        min_num = int(''.join(digits))
        num = max_num - min_num
        cnt += 1

    print(cnt)
    