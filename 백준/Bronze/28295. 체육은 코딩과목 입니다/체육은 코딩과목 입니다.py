import sys

input = sys.stdin.readline

directions = ['N', 'E', 'S', 'W']
result = 0

for _ in range(10):
    command = int(input())
    if command == 1:
        result += 1
    elif command == 2:
        result += 2
    else:
        result -= 1
    result %= 4

print(directions[result])