import sys

input = sys.stdin.readline

scenario = 1

while True:
    command = input().rstrip()
    if command == '0':
        break
    n = int(command)
    students = ['a'] + [input().rstrip() for _ in range(n)]
    found = [0] * (n + 1)
    result = []

    for _ in range(2 * n - 1):
        seize = input().rstrip().split()
        student_num = int(seize[0])
        found[student_num] += 1

    for i in range(1, n + 1):
        if found[i] != 2:
            result.append(students[i])

    print(scenario, *result)
    scenario += 1