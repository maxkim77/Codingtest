def solution(board, h, w):
    # Initialize count to 0
    count = 0
    
    # Define the changes in h and w for neighboring cells
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    # Get the board size
    n = len(board)
    
    # Check each of the four neighbors
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        
        # Check if the neighbor's coordinates are valid
        if 0 <= h_check < n and 0 <= w_check < n:
            # If the neighbor's color is the same, increment count
            if board[h][w] == board[h_check][w_check]:
                count += 1
                
    return count
