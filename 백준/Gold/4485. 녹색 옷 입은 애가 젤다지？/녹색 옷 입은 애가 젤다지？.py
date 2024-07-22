import sys
from heapq import heappush, heappop

input = sys.stdin.readline

dr = (0, 0, -1, 1)
dc = (-1, 1, 0, 0)


def dijkstra(r, c):
    heap = []
    check[r][c] = 0
    heappush(heap, (arr[r][c], 0, 0))  # 최소힙 : arr[r][c]를 기준으로 정렬

    while heap:
        BR, r, c = heappop(heap)  # BR : 최소 루피
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                NBR = BR + arr[nr][nc]
                if check[nr][nc] > NBR:
                    check[nr][nc] = NBR
                    heappush(heap, (NBR, nr, nc))


tc = 0
while True:
    N = int(input())
    if N == 0:
        break

    tc += 1

    arr = [list(map(int, input().split())) for _ in range(N)]
    check = list([987654321] * N for _ in range(N))

    dijkstra(0, 0)

    print(f"Problem {tc}: {check[N - 1][N - 1]}")
