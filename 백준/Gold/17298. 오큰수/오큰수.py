import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
result = [0] * N
mystack = []

for i in range(N):
    while mystack and nums[i] > nums[mystack[-1]]:
        result[mystack.pop()] = nums[i]
    mystack.append(i)

while mystack:
    result[mystack.pop()] = -1

print(*result)