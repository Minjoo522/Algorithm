import sys

input = sys.stdin.readline

a, b, c, d, e = input().rstrip()
result = 0

for num in [a, b, c, d, e]:
    result += int(num) ** 5

print(result)