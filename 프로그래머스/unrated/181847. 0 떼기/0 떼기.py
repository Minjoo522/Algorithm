def solution(n_str):
    i = 0
    while i < len(n_str):
        if n_str[i] != '0':
            break
        i += 1
    return n_str[i:]