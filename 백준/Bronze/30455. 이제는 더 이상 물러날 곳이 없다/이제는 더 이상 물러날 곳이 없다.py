import sys

input = sys.stdin.readline

N = int(input())
print('Duck' if N % 2 == 0 else 'Goose')