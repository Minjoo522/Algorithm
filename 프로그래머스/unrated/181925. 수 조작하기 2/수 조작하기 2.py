def solution(numLog):
    answer = []
    for i in range(len(numLog)-1):
        num = numLog[i+1] - numLog[i]
        if num == 1:
            answer.append('w')
        elif num == -1:
            answer.append('s')
        elif num == 10:
            answer.append('d')
        else:
            answer.append('a')
    return ''.join(answer)