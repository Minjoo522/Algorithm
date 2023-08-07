def solution(my_strings, parts):
    answer = ''
    for i, str in enumerate(my_strings):
        answer += str[parts[i][0]:parts[i][1] + 1]
    return answer