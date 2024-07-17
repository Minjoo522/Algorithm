import sys

sys.setrecursionlimit(10 ** 6)
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


N, M = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(M)]
parent = list(range(N + 1))

edges.sort(key=lambda x: x[2])  # 가중치 기준 오름차순

ans = 0
last_edge = 0
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        ans += c
        last_edge = c

print(ans - last_edge)