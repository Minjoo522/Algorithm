def findVPS(PS):
    if PS[0] == ')':
        return 'NO'

    stack = []
    for ps in PS:
        if ps == '(':
            stack.append(ps)
        if ps == ')':
            if len(stack) == 0:
                return 'NO'
            else:
                stack.pop()

    if len(stack) != 0:
        return 'NO'

    return 'YES'


T = int(input())

for _ in range(T):
    PS = list(input())
    print(findVPS(PS))