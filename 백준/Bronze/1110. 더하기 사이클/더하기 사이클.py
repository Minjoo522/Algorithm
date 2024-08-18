import sys

input = sys.stdin.readline

num = int(input())
a, b = num // 10, num % 10

c, d = b, (a + b) % 10

cnt = 1

while a != c or b != d:
    c, d = d, (c + d) % 10
    cnt += 1
print(cnt)