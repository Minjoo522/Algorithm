import sys

input = sys.stdin.readline

nums = ''.join(input().rstrip().split())
ascending = '12345678'

if nums == ascending:
    print('ascending')
elif nums == ascending[::-1]:
    print('descending')
else:
    print('mixed')