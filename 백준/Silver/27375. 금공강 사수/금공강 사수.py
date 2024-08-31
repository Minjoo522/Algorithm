import sys

input = sys.stdin.readline


def find_combinations(current_combination=[], idx=0):
    result = []

    if sum(current[2] - current[1] + 1 for current in current_combination) == k:
        result.append(current_combination)

    for i in range(idx, n):
        result += find_combinations(current_combination + [lectures[i]], i + 1)

    return result

def is_available(plan):
    plan.sort(key=lambda x: (x[0], x[1]))
    prev_w, prev_s, prev_e = 0, 0, 0
    for p in plan:
        w, s, e = p
        if w == 5:
            return False
        if prev_w == w and prev_e >= s:
            return False
        prev_w, prev_s, prev_e = w, s, e
    return True

n, k = map(int, input().split())
lectures = [tuple(map(int, input().split())) for _ in range(n)]

combinations = find_combinations()

result = 0

for combi in combinations:
    if is_available(combi):
        result += 1

print(result)