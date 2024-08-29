import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    total_len = 0
    correct = 0
    while True:
        command = input()
        if not command.rstrip():
            break
        command = command.rstrip()
        total_len += len(command)
        for char in command:
            if char != '#':
                correct += 1
    result = round(correct / total_len * 100, 1)
    if result.is_integer():
        result = int(result)

    print(f'Efficiency ratio is {result}%.')