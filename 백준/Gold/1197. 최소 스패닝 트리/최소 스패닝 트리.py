import sys

input = sys.stdin.readline


def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


V, E = map(int, input().split())
tree = [tuple(map(int, input().split())) for _ in range(E)]
parent = list(range(V + 1))

tree.sort(key=lambda x: x[2])

ans = 0
for a, b, c in tree:
    if find(a) != find(b):
        union(a, b)
        ans += c

print(ans)