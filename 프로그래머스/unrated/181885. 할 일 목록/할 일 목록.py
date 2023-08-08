def solution(todo_list, finished):
    answer = []
    for i, todo in enumerate(todo_list):
        if finished[i]:
            continue
        answer.append(todo)
    return answer