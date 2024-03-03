import sys

input = sys.stdin.readline

while True:
    str = input().rstrip()
    check = ''
    if str == '.':
        break
    for s in str:
        if s not in '()[]':
            continue
        else:
            check += s
    for _ in range(len(check) // 2 + 1):
        check = check.replace('()', '')
        check = check.replace('[]', '')
    if len(check):
        print('no')
    else:
        print('yes')
