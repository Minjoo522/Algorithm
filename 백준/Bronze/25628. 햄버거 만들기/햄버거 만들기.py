import sys

input = sys.stdin.readline

A, B = map(int, input().split())

print(min(A // 2, B))