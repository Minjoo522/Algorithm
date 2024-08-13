import sys

input = sys.stdin.readline

N = int(input())

cnt = N * (N - 1) // 2

print(cnt * 2)