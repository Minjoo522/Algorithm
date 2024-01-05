import sys

input = sys.stdin.readline


def dfs(now):
    tree[now] = -2

    for after in range(N):
        if tree[after] == now:
            dfs(after)


N = int(input())
tree = list(map(int, input().split()))
K = int(input())

dfs(K)
cnt = 0

for i in range(N):
    if tree[i] != -2 and i not in tree:
        cnt += 1

print(cnt)