def solution(sizes):
    max_width = 0
    max_height = 0
    
    for size in sizes:
        width, height = size
        
        # 현재 명함의 가로 길이와 세로 길이 중에서 큰 값과 작은 값을 구합니다.
        max_dim = max(width, height)
        min_dim = min(width, height)
        
        # 현재 명함의 큰 값이 최대 가로 길이보다 크다면 갱신
        if max_dim > max_width:
            max_width = max_dim
            
        # 현재 명함의 작은 값이 최대 세로 길이보다 크다면 갱신
        if min_dim > max_height:
            max_height = min_dim
            
    # 가로 길이와 세로 길이를 곱해 최소 지갑 크기를 구함
    answer = max_width * max_height
    return answer
