import sys

input = sys.stdin.readline

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

start = 1  # 랜선의 길이는 1 이상어야 한다.
end = max(lines)
result = 0

while start <= end:
    mid = (start + end) // 2

    total = sum(line // mid for line in lines)

    if total >= N:  # N개 이상의 랜선을 만들 수 있다면 더 긴길이도 가능한지 확인
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
