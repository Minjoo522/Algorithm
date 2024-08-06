import sys

input = sys.stdin.readline

N = int(input())
original = input().rstrip()
duramuri = input().rstrip()
aeiou = 'aeiou'

if original[-1] != duramuri[-1] or original[0] != duramuri[0] or sorted(original) != sorted(duramuri):
    print('NO')
    exit(0)

new_original = ''
for o in original:
    if o not in aeiou:
        new_original += o

new_duramuri = ''
for d in duramuri:
    if d not in aeiou:
        new_duramuri += d

if new_original != new_duramuri:
    print('NO')
else:
    print('YES')
