import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
S = [0] * N  # 합 배열
C = [0] * M  # 업데이트 된 합 배열 중 동일한 값을 가진 애들이 몇 개인지 저장하는 배열
ans = 0

S[0] = nums[0]
# 누적 합
for i in range(1, N):
    S[i] = nums[i] + S[i - 1]

# 합 배열 업데이트
for i in range(N):
    remainder = S[i] % M
    if remainder == 0:
        ans += 1
    C[remainder] += 1

for i in range(M):
    if C[i] > 1:  # 같은 나머지 값을 갖는 애가 2개 이상 있으면
        ans += C[i] * (C[i] - 1) // 2  # combiantion 공식 (무조건 2개)

print(ans)