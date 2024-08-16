import sys

input = sys.stdin.readline

for _ in range(int(input())):
    year = input().rstrip()
    last_two = int(year[2:])
    if (int(year) + 1) % last_two == 0:
        print('Good')
    else:
        print('Bye')
