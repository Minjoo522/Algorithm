def solution(ineq, eq, n, m):
    if ineq == ">" and eq == "=":
        answer = int(n >= m)
    elif ineq == "<" and eq == "=":
        answer = int(n <= m)
    elif ineq == ">" and eq == "!":
        answer = int(n > m)
    else:
        answer = int(n < m)
    return answer