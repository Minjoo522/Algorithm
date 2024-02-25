import sys

input = sys.stdin.readline

for _ in range(int(input())):
    money = [25, 10, 5, 1]
    result = [0 for _ in range(4)]
    change = int(input())

    for i in range(4):
        result[i], change = divmod(change, money[i])

    print(*result)
