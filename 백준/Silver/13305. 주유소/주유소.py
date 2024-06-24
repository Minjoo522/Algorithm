import sys

input = sys.stdin.readline

N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_price = prices[0]
result = prices[0] * distances[0]

for current in range(1, N - 1):
    if min_price > prices[current]:
        min_price = prices[current]

    result += min_price * distances[current]

print(result)