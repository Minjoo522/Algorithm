import sys

input = sys.stdin.readline

M = int(input())
N = int(input())

primes = []
for i in range(M, N + 1):
    if i < 2:
        continue
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))
