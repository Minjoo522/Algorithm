import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
dic = {x: i for i, x in enumerate(sorted(set(arr)))}
ans = [dic[x] for x in arr]

print(*ans)
