import sys

input = sys.stdin.readline

alpa_to_num = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8
}
line = [1, 0] * 4
board = [[0] * 9]
board.extend([[0] + (line if i % 2 != 0 else line[::-1]) for i in range(1, 9)])

for _ in range(int(input())):
    word, num = input().rstrip().split()
    x, y = alpa_to_num[word[0]], int(word[-1])
    num = int(num)
    if board[x][y] == board[(num - 1) // 8 + 1][(num - 1) % 8 + 1]:
        print('YES')
    else:
        print('NO')
