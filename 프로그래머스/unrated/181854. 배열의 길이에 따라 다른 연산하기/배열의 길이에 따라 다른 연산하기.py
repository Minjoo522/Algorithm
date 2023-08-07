def solution(arr, n):
    if len(arr) % 2 == 0:
        range_start = 1
    else:
        range_start = 0
    for i in range(range_start, len(arr), 2):
            arr[i] = arr[i] + n
    return arr