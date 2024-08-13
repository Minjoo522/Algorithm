import sys

input = sys.stdin.readline

N = int(input())
word = 'a' + input().rstrip()

cnt = 0

for i in range(1, N // 2 + 1):
    if word[i] != word[-i]:
        cnt += 1

print(cnt)