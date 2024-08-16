import sys

input = sys.stdin.readline

alpha = 'abcdefghijklmnopqrstuvwxyz'

while True:
    sentence = input().rstrip()
    if sentence == '#':
        break

    unique = set()
    for char in sentence:
        if char.lower() in alpha:
            unique.add(char.lower())
    print(len(unique))
