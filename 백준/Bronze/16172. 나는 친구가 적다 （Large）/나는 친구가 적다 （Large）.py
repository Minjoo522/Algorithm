import sys

input = sys.stdin.readline

S = input().rstrip()
keyword = input().rstrip()

for i in range(10):
    S = S.replace(str(i), '')
    
print(1 if keyword in S else 0)