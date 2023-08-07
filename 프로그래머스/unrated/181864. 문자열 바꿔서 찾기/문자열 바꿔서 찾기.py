def solution(myString, pat):
    answer = ''
    for n in myString:
        if n == 'A':
            answer += 'B'
        elif n == 'B':
            answer += 'A'
    return int(pat in answer)