import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))
ans = []

while q:
    idx, paper = q.popleft();
    ans.append(idx + 1)

    if paper > 0:
        q.rotate(-(paper - 1))  # 현재 풍선을 pop했기 때문에 왼쪽으로 1칸씩 회전된 상태
    elif paper < 0:
        q.rotate(-paper)

print(*ans)