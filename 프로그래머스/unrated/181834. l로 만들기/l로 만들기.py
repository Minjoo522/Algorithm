def solution(myString):
    answer = ''
    for str in myString:
        if str < 'l':
            answer += 'l'
            continue
        answer += str
    return answer