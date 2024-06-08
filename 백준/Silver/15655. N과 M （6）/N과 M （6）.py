import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
sel = [0] * M


def combination(idx, sidx):
    if sidx == M:
        print(*sel)
        return

    if idx == N:
        return

    sel[sidx] = nums[idx]
    combination(idx + 1, sidx + 1)
    combination(idx + 1, sidx)


combination(0, 0)
