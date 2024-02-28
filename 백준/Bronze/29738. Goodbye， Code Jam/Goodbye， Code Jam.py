import sys

input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    rank = int(input())
    ans = ""

    if rank > 4500:
        ans = "Round 1"
    elif rank > 1000:
        ans = "Round 2"
    elif rank > 25:
        ans = "Round 3"
    else:
        ans = "World Finals"

    print(f"Case #{tc}: {ans}")
