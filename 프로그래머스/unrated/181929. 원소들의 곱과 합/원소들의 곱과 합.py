def solution(num_list):
    return int(int(eval('*'.join(map(str, num_list)))) < sum(num_list)**2)