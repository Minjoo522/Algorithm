import sys

input = sys.stdin.readline

while True:
    command = input().rstrip()
    if command == '#':
        break

    target = command.split()[0]
    sentences = command.split()[1:]

    cnt = 0

    for sentence in sentences:
        for char in sentence:
            if char.lower() == target:
                cnt += 1

    print(target, cnt)