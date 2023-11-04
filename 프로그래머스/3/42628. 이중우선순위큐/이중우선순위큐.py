import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    count = 0  # 힙에 있는 요소의 수를 추적합니다.
    
    for operation in operations:
        command, value = operation.split()  # 명령어와 값을 분리합니다.
        value = int(value)
        
        if command == "I":  # 삽입 연산
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)
            count += 1
        elif count > 0:  # 힙이 비어있지 않은 경우 삭제 연산 수행
            if value == 1:  # 최댓값 삭제
                heapq.heappop(max_heap)
            else:  # 최솟값 삭제
                heapq.heappop(min_heap)
            count -= 1
            
            # 동기화: 최소 힙과 최대 힙의 요소 수가 다를 경우 재정렬합니다.
            if count == 0:
                min_heap = []
                max_heap = []

    if count > 0:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    else:
        return [0, 0]