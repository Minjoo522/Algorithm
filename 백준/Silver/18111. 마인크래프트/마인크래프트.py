import sys

input = sys.stdin.readline

from collections import defaultdict

N, M, B = map(int, input().split())

height_info = defaultdict(int)

top, bottom = -1, 257

for _ in range(N):
    for height in list(map(int, input().split())):
        height_info[height] += 1
        top = max(top, height)  # 최대 값
        bottom = min(bottom, height)  # 최소 값

ans = [987654321, -1]  # 시간, 땅의 높이 초기화

for standard in range(top, bottom - 1, -1):  # top, bottom 범위 돌면서
    need_blocks = 0
    add_blocks = 0

    for key, value in height_info.items():
        height_diff = standard - key  # 기준 값과 높이 비교

        if height_diff < 0:  # 기준 높이가 더 낮을 때
            add_blocks -= height_diff * value  # 깎기

        if height_diff > 0:  # 기준 높이가 더 높을 때
            need_blocks += height_diff * value  # 쌓기

    if need_blocks > B + add_blocks:  # 필요한 블럭의 개수 > 인벤토리 + 새로 얻을 블럭 => 불가능
        continue
    
    cnt = need_blocks + (add_blocks * 2)
    
    if cnt < ans[0]:  # 최소 시간 찾기
        ans = [cnt, standard]
        
print(*ans)