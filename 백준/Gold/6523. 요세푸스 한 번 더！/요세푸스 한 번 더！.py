import sys

input = sys.stdin.readline

from collections import defaultdict

while True:
    command = input().rstrip()
    if command == '0':
        break

    N, a, b = map(int, command.split())
    x = 0
    people = defaultdict(int)

    while True:
        x = (a * x * x + b) % N
        people[x] += 1
        if people[x] == 3:
            break

    one = list(people.values()).count(1)  # 한 번만 선택된 사람
    print(N - len(people) + one)  # N - len(people) 한 번도 선택되지 않은 사람 + 한 번만 선택된 사람
