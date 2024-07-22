import sys
import heapq

input = sys.stdin.readline

N = int(input())
cards = [int(input()) for _ in range(N)]
heapq.heapify(cards)

result = 0

while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    heapq.heappush(cards, a + b)
    result += a + b

print(result)