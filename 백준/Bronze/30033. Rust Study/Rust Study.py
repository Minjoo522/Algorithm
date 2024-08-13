import sys

input = sys.stdin.readline

N = int(input())
plan = list(map(int, input().split()))
real = list(map(int, input().split()))

print(sum(1 for i in range(N) if plan[i] <= real[i]))
