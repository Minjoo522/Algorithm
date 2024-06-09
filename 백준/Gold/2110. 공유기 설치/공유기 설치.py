import sys

input = sys.stdin.readline

N, C = map(int, input().split())
houses = sorted(int(input()) for _ in range(N))


def binary_search(arr, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = arr[0]
        count = 1

        for i in range(1, len(arr)):
            if arr[i] >= current + mid:
                count += 1
                current = arr[i]

        if count >= C:
            global ans
            start = mid + 1
            ans = mid
        else:
            end = mid - 1


start = 1
end = houses[-1] - houses[0]
ans = 0

binary_search(houses, start, end)
print(ans)
