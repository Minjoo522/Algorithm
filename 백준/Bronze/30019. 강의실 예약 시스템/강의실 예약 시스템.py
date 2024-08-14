import sys

input = sys.stdin.readline

N, M = map(int, input().split())
classrooms = [0] * (N + 1)

for _ in range(M):
    k, s, e = map(int, input().split())
    if classrooms[k] <= s:
        classrooms[k] = e
        print('YES')
    else:
        print('NO')