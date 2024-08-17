import sys
from collections import Counter

input = sys.stdin.readline

bronzesilver = 'BRONZESILVER'
bronzesilver_count = Counter(bronzesilver)

N = int(input())
seals = input().rstrip()

seals_count = Counter(seals)

min_snacks = 987654321
for char in bronzesilver_count:
    if seals_count[char] == 0:
        min_snacks = 0
        break
    min_snacks = min(min_snacks, seals_count[char] // bronzesilver_count[char])

print(min_snacks)