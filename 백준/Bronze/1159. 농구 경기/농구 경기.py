import sys
from collections import defaultdict

input = sys.stdin.readline

names = defaultdict(int)

for _ in range(int(input())):
    names[input()[0]] += 1

result = ''.join(sorted(name for name, count in names.items() if count >= 5))
print(result if result else 'PREDAJA')