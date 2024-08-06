import sys

input = sys.stdin.readline


def binary_search(power):
    left, right = 0, N - 1

    while left <= right:
        mid = (left + right) // 2

        if titles[mid][1] < power:
            left = mid + 1
        else:
            right = mid - 1
    return titles[left][0]


N, M = map(int, input().split())
titles = list(map(lambda x: (x[0], int(x[1])), (input().split() for _ in range(N))))

for _ in range(M):
    power = int(input())
    print(binary_search(power))
