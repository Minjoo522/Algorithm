import sys

input = sys.stdin.readline

N = int(input())
first_round = list(map(int, input().split()))
second_round = list(map(int, input().split()))

result = sum(abs(num) for num in first_round) - sum(-abs(num) for num in second_round)
print(result)