import heapq

def solution(jobs):
    jobs.sort()  # 요청 시간에 따라 정렬
    length = len(jobs)
    time, end, queue = 0, -1, []
    wait_times = 0  # 총 대기 시간

    # 아직 처리하지 않은 작업이 있거나 대기열에 작업이 있으면 계속 반복
    while len(jobs) > 0 or len(queue) > 0:
        # 현재 시간 내에 처리할 수 있는 모든 작업을 대기열에 넣음
        while len(jobs) > 0 and jobs[0][0] <= time:
            job = jobs.pop(0)
            # 실행 시간 기준으로 최소 힙을 유지하기 위해 (작업 시간, 요청 시간) 순으로 넣음
            heapq.heappush(queue, (job[1], job[0]))
        
        # 대기열에 작업이 있으면 하나를 꺼내 처리
        if len(queue) > 0:
            current = heapq.heappop(queue)
            start = current[1]
            wait = time - start
            wait_times += wait + current[0]  # 대기 시간 + 작업 시간
            time += current[0]  # 현재 시간 갱신
        else:
            time += 1  # 대기열에 작업이 없으면 시간을 1 증가

    return wait_times // length  # 평균 대기 시간

