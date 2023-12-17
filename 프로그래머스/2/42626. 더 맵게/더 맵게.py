import heapq

def solution(scoville, K):
    heapq.heapify(scoville) 
    mix_count = 0
    
    while True:
        first_min = heapq.heappop(scoville)
        
        if first_min >= K:
            return mix_count
        
        if not scoville:
            return -1
        
        second_min = heapq.heappop(scoville)
        new_scoville = first_min + (second_min *2)
        heapq.heappush(scoville, new_scoville)
        mix_count += 1
        
    return mix_count
        