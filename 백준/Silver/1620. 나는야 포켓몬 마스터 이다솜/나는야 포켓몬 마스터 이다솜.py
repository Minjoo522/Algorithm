import sys

input = sys.stdin.readline

N, M = map(int, input().split())
pocketmons = {}

for i in range(1, N + 1):
    pocketmon = input().rstrip()
    pocketmons[pocketmon] = i
    pocketmons[str(i)] = pocketmon

for _ in range(M):
    print(pocketmons[input().rstrip()])
