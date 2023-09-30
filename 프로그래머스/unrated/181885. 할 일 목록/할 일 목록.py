def solution(todo_list, finished):
    answer = []
    for todo, is_finished in zip(todo_list, finished):
        if not is_finished:
            answer.append(todo)
    
    return answer