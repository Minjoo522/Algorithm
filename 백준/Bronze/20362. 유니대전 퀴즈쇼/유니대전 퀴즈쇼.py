import sys

input = sys.stdin.readline

N, S = input().rstrip().split()
answer = ''
cnt = 0
chats = []

for i in range(int(N)):
    nickname, desc = input().rstrip().split()
    if nickname == S:
        answer = desc
        cnt = i
    else:
        chats.append(desc)

result = 0
for i in range(cnt):
    if chats[i] == answer:
        result += 1

print(result)