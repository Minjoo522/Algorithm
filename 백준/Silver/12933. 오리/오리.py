import sys

input = sys.stdin.readline
quack = 'quack'
sound = input().rstrip()
visited = [0] * len(sound)
cnt = 0

if not sound.startswith('q') or not sound.endswith('k') or len(sound) % 5:
    print(-1)
    sys.exit(0)


def find_quack(start):
    global cnt
    idx = 0
    flag = True
    for i in range(start, len(sound)):
        if sound[i] == quack[idx] and visited[i] == 0:
            visited[i] = 1
            if quack[idx] == 'k':
                if flag:
                    cnt += 1
                    flag = False
                idx = 0
            else:
                idx += 1


for i in range(len(sound)):
    find_quack(i)

if cnt == 0 or not all(visited):
    print(-1)
else:
    print(cnt)