import sys

input = sys.stdin.readline

def count_dots(n):
    if n == 1:
        return 5
    dots = 5
    for i in range(2, n + 1):
        dots += 3 * i + 1
    return dots

print(count_dots(int(input())) % 45678)