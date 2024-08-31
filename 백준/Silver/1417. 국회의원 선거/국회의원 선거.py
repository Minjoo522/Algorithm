import sys

input = sys.stdin.readline

N = int(input())
dasom = int(input())
votes = [int(input()) for _ in range(N - 1)]
votes.sort(reverse=True)

result = 0

if len(votes) == 0:
    print(0)
    sys.exit()

while dasom <= votes[0]:
    result += 1
    dasom += 1
    votes[0] -= 1
    votes.sort(reverse=True)

print(result)