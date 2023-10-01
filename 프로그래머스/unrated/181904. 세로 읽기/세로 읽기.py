def solution(my_string, m, c):
    strings = []
    row = len(my_string)//m
    for i in range(0, row):
        strings.append(my_string[i*m:m*(i+1)])
    answer = ''.join([str[c-1] for str in strings])
    return answer