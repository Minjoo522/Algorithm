import sys

input = sys.stdin.readline

N = int(input())
candies = list(map(int, input().split()))
odd = [candy for candy in candies if candy % 2 != 0]

total = sum(candies)

if total % 2 == 0:
    print(total)
else:
    if odd:
        total -= min(odd)
        print(total)
    else:
        print(0)