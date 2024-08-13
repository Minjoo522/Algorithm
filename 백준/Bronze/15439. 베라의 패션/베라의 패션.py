import sys
from itertools import combinations

input = sys.stdin.readline

cloths = [i for i in range(int(input()))]

print(sum(1 for _ in combinations(cloths, 2)) * 2)