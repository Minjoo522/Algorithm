import sys

input = sys.stdin.readline

MOD = 10 ** 9 + 7

def mat_mult(A, B):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]]


def mat_pow(M, power):
    result = [[1, 0], [0, 1]]
    base = M

    while power > 0:
        if power % 2 == 1:
            result = mat_mult(result, base)
        base = mat_mult(base, base)
        power //= 2

    return result


def solve(N):
    if N == 1:
        return 3

    transform_matrix = [[2, 2], [1, 0]]

    result_matrix = mat_pow(transform_matrix, N - 1)

    prev_0, prev_1 = 2, 1

    final_0 = (result_matrix[0][0] * prev_0 + result_matrix[0][1] * prev_1) % MOD
    final_1 = (result_matrix[1][0] * prev_0 + result_matrix[1][1] * prev_1) % MOD

    return (final_0 + final_1) % MOD


N = int(input())

print(solve(N))
