import sys

input = sys.stdin.readline

word = input().rstrip()
uppers = input().rstrip().split()

result = ''

for w in word:
    if w in uppers:
        result += w.lower()
    else:
        result += w

print(result)