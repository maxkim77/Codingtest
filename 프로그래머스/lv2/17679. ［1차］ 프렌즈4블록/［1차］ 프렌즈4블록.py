def solution(m, n, board):
    answer = 0
    # board를 2차원 리스트로 변환
    board = [list(row) for row in board]
    
    # 블록이 제거되었는지를 판단하는 플래그
    removed = True
    while removed:
        removed = []
        # 제거할 블록들을 찾기
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != '':
                    removed += [(i, j), (i, j+1), (i+1, j), (i+1, j+1)]
                    
        # 중복 제거 후 실제 블록 제거
        for i, j in set(removed):
            board[i][j] = ''
            answer += 1
        
        # 블록 아래로 내리기
        for j in range(n):
            stack = [board[i][j] for i in range(m) if board[i][j] != '']
            for i in range(m-1, -1, -1):
                board[i][j] = stack.pop() if stack else ''
    
    return answer
