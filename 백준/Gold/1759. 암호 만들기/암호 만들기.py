import sys
input = sys.stdin.readline

from itertools import combinations

vowels_standard = ['a', 'e', 'i', 'o', 'u']

L, C = map(int, input().split())
letters = list(input().split())

vowels = []
consonants = []

for letter in letters:
    if letter in vowels_standard:
        vowels.append(letter)
    else:
        consonants.append(letter)

passwords = []

for v in range(1, L-1):
    for vowel in combinations(vowels, v):
        for consonant in combinations(consonants, L-v):
            tmp = sorted(list(vowel + consonant))
            passwords.append(tmp)

passwords.sort()

for password in passwords:
    print(''.join(password))