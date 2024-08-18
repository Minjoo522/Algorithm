import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
S = '0' + input().rstrip()
infections = set()

for i in range(1, N + 1):
    if S[i] == 'R':
        left = max(1, i - K)
        right = min(N, i + K)
        for j in range(left, right + 1):
            infections.add(j)

if len(infections) <= M:
    print('Yes')
else:
    print('No')