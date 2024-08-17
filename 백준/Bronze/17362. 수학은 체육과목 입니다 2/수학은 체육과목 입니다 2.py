import sys

input = sys.stdin.readline

fingers = [1, 2, 3, 4, 5, 4, 3, 2]

N = int(input())

print(fingers[(N - 1) % 8])