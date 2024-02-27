import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(i)

count = 0
for i in permutations(arr, N):
    count += 1

print(count)
