import sys

input = sys.stdin.readline

N = int(input())
ans = 0
check = [0] * N


def n_queen(depth):
    global ans

    if depth == N:
        ans += 1
        return

    for i in range(N):
        check[depth] = i
        for j in range(depth):
            if check[j] == check[depth] or abs(depth - j) == abs(check[depth] - check[j]):
                break
        else:
            n_queen(depth + 1)


n_queen(0)

print(ans)
