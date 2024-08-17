import sys

input = sys.stdin.readline

W, P = map(int, input().split())
partitions = [0] + list(map(int, input().split())) + [W]

sizes = set()

for i in range(0, len(partitions) - 1):
    for j in range(i + 1, len(partitions)):
        sizes.add(partitions[j] - partitions[i])

print(*sorted(sizes))