import sys

input = sys.stdin.readline

N, B = map(int, input().split())

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

current = N
result = ""

while current > 0:
    current, remainder = divmod(current, B)  # a를 b로 나눈 몫과 나머지를 반환
    result = digits[remainder] + result

print(result)
