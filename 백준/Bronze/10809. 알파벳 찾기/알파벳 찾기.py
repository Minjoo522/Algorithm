import sys

input = sys.stdin.readline

word = input().rstrip()
alphabet_in_word = []

for char in range(ord('a'), ord('z') + 1):
    alphabet = chr(char)
    if alphabet in word:
        alphabet_in_word.append(word.index(alphabet))
    else:
        alphabet_in_word.append(-1)

print(*alphabet_in_word)
