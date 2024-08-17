import sys

input = sys.stdin.readline

sentence = input().rstrip()

if len(sentence) < 4:
    print(0)
    sys.exit()

total = 0

for i in range(0, len(sentence) - 4 + 1):
    if sentence[i:i + 4] == 'DKSH':
        total += 1

print(total)