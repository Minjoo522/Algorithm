import sys
import math

input = sys.stdin.readline

M = int(input())
N = int(input())

def find_perfect_squares(start, end):
    perfect_squares = []
    for num in range(start, end + 1):
        sqrt_num = int(math.sqrt(num))
        if sqrt_num * sqrt_num == num:
            perfect_squares.append(num)
    return perfect_squares

perfect_squares = find_perfect_squares(M, N)
if perfect_squares:
    print(sum(perfect_squares))
    print(min(perfect_squares))
else:
    print(-1)