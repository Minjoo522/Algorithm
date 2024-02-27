import sys
input = sys.stdin.readline

coordinates = [tuple(map(int, input().split())) for _ in range(int(input()))]
coordinates.sort()

for coordinate in coordinates:
    print(*coordinate)