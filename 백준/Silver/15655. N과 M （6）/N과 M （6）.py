import sys

input = sys.stdin.readline


def combination(idx, sidx):
    if sidx == M:
        print(*ans)
        return

    if idx == N:
        return

    ans[sidx] = nums[idx]
    combination(idx + 1, sidx + 1)
    combination(idx + 1, sidx)


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = [0] * M

combination(0, 0)