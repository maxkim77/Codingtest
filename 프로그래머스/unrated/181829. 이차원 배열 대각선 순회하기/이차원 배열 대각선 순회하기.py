def solution(board, k):
    # 초기 답을 0으로 설정합니다.
    answer = 0
    
    # board의 모든 행에 대해 반복합니다.
    for i in range(len(board)):
        # 현재 행의 모든 열에 대해 반복합니다.
        for j in range(len(board[i])):
            # 현재 위치의 행과 열의 합이 k 이하인 경우
            if i + j <= k:
                # 해당 위치의 값을 answer에 더합니다.
                answer += board[i][j]
    
    # 최종 결과를 반환합니다.
    return answer
