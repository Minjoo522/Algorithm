import sys

input = sys.stdin.readline

N = int(input())
current = list(map(int, input().split()))
tmp = []
target = 1

for i in current:
    tmp.append(i)
    while tmp and tmp[-1] == target:
        tmp.pop()
        target += 1
    if len(tmp) > 1 and tmp[-1] > tmp[-2]:
        print('Sad')
        sys.exit()
if tmp:
    print('Sad')
else:
    print('Nice')
