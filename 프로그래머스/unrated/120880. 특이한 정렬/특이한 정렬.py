def solution(numlist, n):
    #정렬기준을 정의하는 함수
    def sort_key(value):
        distance = abs(value - n) #n으로부터 거리계산
        #거리와 -value를 반환하여 거리가 작은 순서대로, 거리가 같으면 큰숫자가 반환
        return (distance, -value)
        
    return sorted(numlist, key=sort_key)