str = input()
result_list = []

for i in str:
    if i.islower():
        result_list.append(i.upper())
    else:
        result_list.append(i.lower())
        
result = ''.join(i for i in result_list)
print(result)