import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
fruits = list(map(int, input().split()))

low = 0
result = 0
cnt = 0
tanghulu = defaultdict(int)

for high in range(N):
    tanghulu[fruits[high]] += 1

    # 새로운 숫자 : 과일 개수 증가
    if tanghulu[fruits[high]] == 1:
        cnt += 1

    # 과일 개수가 2보다 크면 low 증가 -> 슬라이딩 윈도우 줄임
    while cnt > 2:
        tanghulu[fruits[low]] -= 1
        if tanghulu[fruits[low]] == 0:
            cnt -= 1
        low += 1

    result = max(result, high - low + 1)

print(result)