def solution(array, n):
    closest = None #가장 가까운 수를 저장할 변수
    min_distance = float('inf') #초기 최소 거리를 무한대로 설정
    
    for num in array:
        distance = abs(num-n) #현재 원소와 n사이 거리 계산
        if distance < min_distance: #현재 거리가 최소거리 보다 작으면 업데이트
            closest = num
            min_distance = distance
        elif distance == min_distance: #동일한 거리를 가지는 경우 더 작은 값으로 업데이트
            closest = min(closest, num)
    return closest