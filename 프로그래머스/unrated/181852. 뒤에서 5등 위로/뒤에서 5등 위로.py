def solution(num_list):
    num_list.sort(reverse=True)
    i = 0
    while i < 5:
        num_list.pop()
        i += 1
    num_list.sort()
    return num_list