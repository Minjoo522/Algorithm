import sys

input = sys.stdin.readline

dial = ["", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
word = input().rstrip()

time = 0

for char in word:
    for i in range(len(dial)):
        if char in dial[i]:
            time += 2 + i - 1

print(time)
