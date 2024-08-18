import sys

input = sys.stdin.readline

S = input().rstrip()
nums = '1234567890'
sentences = ''

for char in S:
    if char not in nums:
        sentences += char

keyword = input().rstrip()
if keyword in sentences:
    print(1)
else:
    print(0)