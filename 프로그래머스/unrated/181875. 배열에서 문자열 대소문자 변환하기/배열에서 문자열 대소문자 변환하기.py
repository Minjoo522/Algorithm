def solution(strArr):
    for i, str in enumerate(strArr):
        if i % 2 == 0:
            strArr[i] = str.lower()
        else:
            strArr[i] = str.upper()
    return strArr