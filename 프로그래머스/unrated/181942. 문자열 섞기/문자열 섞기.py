def solution(str1, str2):
    str_list = []
    for i in str1:
        str_list.append(i)
    for i, e in enumerate(str2):
        str_list.insert(2 * i + 1 , e)
    answer = ''.join(str_list)
    return answer