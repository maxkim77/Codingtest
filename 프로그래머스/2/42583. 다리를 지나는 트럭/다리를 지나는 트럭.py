from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    #다리를 거너는 트럭 관리 하기위해 큐를 초기화 
    # 큐에는 트럭의 무게와 함께 다리를 건너기시작한 시간을 저장
    bridge_queue = deque([0] * bridge_length)
    total_weight =0 # 현재 다리 위의 트럭 무게 합계
    time = 0 # 총소요시간
    truck_index = 0 # 대기중인 트럭의 인덱스
    
    while truck_index < len(truck_weights):
        time += 1 #시간을 1 증가시킵니다.
        total_weight -= bridge_queue.popleft()
        #다음 트럭이 다리위에 올라갈 수 있는지 확인합니다.
        if total_weight + truck_weights[truck_index] <= weight:
            bridge_queue.append(truck_weights[truck_index]) #다리 큐에트럭을 추가합니다.
            total_weight += truck_weights[truck_index]
            truck_index += 1 #다음트럭으로 인덱스 이동
        else:
            bridge_queue.append(0) #트럭이 올라갈수 없다면 0을 추가
    time += bridge_length
    return time