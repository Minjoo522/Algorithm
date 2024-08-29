import sys

input = sys.stdin.readline

def is_magic_square(matrix, N):
    flattened = [num for row in matrix for num in row]
    if len(set(flattened)) != N * N or any(num <= 0 or num > N ** 2 for num in flattened):
        return False

    magic_sum = N * (N ** 2 + 1) // 2

    for i in range(N):
        if sum(matrix[i]) != magic_sum or sum(matrix[j][i] for j in range(N)) != magic_sum:
            return False

    if sum(matrix[i][i] for i in range(N)) != magic_sum or sum(matrix[i][N - i - 1] for i in range(N)) != magic_sum:
        return False

    return True

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

if is_magic_square(matrix, N):
    print('TRUE')
else:
    print('FALSE')