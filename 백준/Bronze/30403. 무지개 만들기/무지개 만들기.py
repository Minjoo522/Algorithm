import sys

input = sys.stdin.readline

lower_rb = 'roygbiv'
upper_rb = 'ROYGBIV'

N = int(input())
word = input().rstrip()

lower = ''.join([char for char in lower_rb if char in word])
upper = ''.join([char for char in upper_rb if char in word])

if lower == lower_rb and upper == upper_rb:
    print('YeS')
elif lower == lower_rb and upper != upper_rb:
    print('yes')
elif lower != lower_rb and upper == upper_rb:
    print('YES')
else:
    print('NO!')