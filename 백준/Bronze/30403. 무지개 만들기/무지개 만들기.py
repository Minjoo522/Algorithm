import sys

input = sys.stdin.readline

lower_rb = set('roygbiv')
upper_rb = set('ROYGBIV')

N = int(input())
word = input().rstrip()

word_set = set(word)

has_lower = lower_rb.issubset(word_set)
has_upper = upper_rb.issubset(word_set)

if has_lower and has_upper:
    print('YeS')
elif has_lower:
    print('yes')
elif has_upper:
    print('YES')
else:
    print('NO!')
