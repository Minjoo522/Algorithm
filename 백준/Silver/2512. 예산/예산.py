import sys

input = sys.stdin.readline

N = int(input())
moneys = list(map(int, input().split()))
M = int(input())

start = 1
end = max(moneys)
result = 0

while start <= end:
    mid = (start + end) // 2

    total = sum(mid if money > mid else money for money in moneys)

    if total <= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)