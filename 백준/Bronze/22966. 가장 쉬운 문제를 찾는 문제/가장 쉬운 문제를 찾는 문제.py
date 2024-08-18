import sys

input = sys.stdin.readline

problems = {}

for _ in range(int(input())):
    problem, level = input().rstrip().split()
    problems[level] = problem

lowest = min(problems.keys())
print(problems[lowest])