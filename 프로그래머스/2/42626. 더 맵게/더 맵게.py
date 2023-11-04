import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # scoville 배열을 힙으로 변환
    mix_count = 0  # 섞은 횟수

    while True:
        first_min = heapq.heappop(scoville)  # 가장 낮은 스코빌 지수를 가진 음식
        
        # 첫 번째로 낮은 스코빌 지수가 K 이상이면 모든 음식이 K 이상임을 의미
        if first_min >= K:
            return mix_count
        
        # 음식이 하나밖에 없는데 스코빌 지수가 K 미만이면 더 이상 섞을 수 없으므로 -1을 반환
        if not scoville:
            return -1
        
        second_min = heapq.heappop(scoville)  # 두 번째로 낮은 스코빌 지수를 가진 음식
        new_scoville = first_min + (second_min * 2)  # 새로운 스코빌 지수 계산
        heapq.heappush(scoville, new_scoville)  # 계산된 스코빌 지수를 힙에 다시 삽입
        mix_count += 1  # 섞은 횟수 증가

    return mix_count

