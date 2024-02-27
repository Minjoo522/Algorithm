import sys

input = sys.stdin.readline

A, B = map(int, input().split())
K, X = map(int, input().split())

people = [i for i in range(A, B + 1)]
ans = 0

for p in people:
    if abs(K - p) <= X:
        ans += 1

if ans == 0:
    print("IMPOSSIBLE")
else:
    print(ans)
