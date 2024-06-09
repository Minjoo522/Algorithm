import sys
import bisect

input = sys.stdin.readline

N, M = map(int, input().split())
points = sorted(map(int, input().split()))

for _ in range(M):
    start, end = map(int, input().split())
    left_index = bisect.bisect_left(points, start)  # start 이상인 첫 위치
    right_index = bisect.bisect_right(points, end)  # end 이하인 마지막 위치
    result = right_index - left_index
    print(result)
    