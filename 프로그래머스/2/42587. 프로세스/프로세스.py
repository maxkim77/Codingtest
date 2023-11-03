from collections import deque

def solution(priorities, location):
    queue = deque([(priority, i) for i, priority in enumerate(priorities)])
    answer = 0
    while True:
        current = queue.popleft() #큐에서 프로세스를 하나 꺼냄
        if any(current[0] < q[0] for q in queue):
            #현재 프로세스보다 우선순위가 높은 프로세스가 있다면 다시 큐에 넣음
            queue.append(current)
        else:
            answer += 1
            if current[1] == location:
                return answer

