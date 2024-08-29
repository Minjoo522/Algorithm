import sys

input = sys.stdin.readline

scenario = 1

while True:
    command = input().rstrip()
    if command == '0':
        break
    
    n = int(command)
    students = [input().rstrip() for _ in range(n)]
    found = [0] * n

    for _ in range(2 * n - 1):
        student_num, _ = input().rstrip().split()
        found[int(student_num) - 1] += 1

    print(scenario, students[found.index(1)])
    scenario += 1