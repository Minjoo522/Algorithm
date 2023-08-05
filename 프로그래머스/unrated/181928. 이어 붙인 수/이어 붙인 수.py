def solution(num_list):
    even = []
    odd = []
    for num in num_list:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    answer = int(''.join(map(str, even))) + int(''.join(map(str, odd)))
    return answer