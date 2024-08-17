import sys

input = sys.stdin.readline

for _ in range(int(input())):
    scores = list(map(int, input().split()))
    scores.sort()
    trimmed_scores = scores[1:-1]

    if max(trimmed_scores) - min(trimmed_scores) >= 4:
        print('KIN')
    else:
        print(sum(trimmed_scores))
