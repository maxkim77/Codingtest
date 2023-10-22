def solution(keyinput, board):
    x, y = 0, 0
    max_x, max_y = (board[0] - 1) // 2, (board[1] -1) // 2
    for key in keyinput:
        new_x, new_y = x, y
        if key == "up":
            new_y += 1
        elif key == "down":
            new_y -= 1
        elif key == "left":
            new_x -= 1
        elif key == "right":
            new_x += 1
        # 새로운 좌표가 맵의 크기를 벗어나지 않는지 확인
        if -max_x <= new_x <= max_x and -max_y <= new_y <= max_y:
            x, y = new_x, new_y  # 캐릭터의 좌표를 업데이트

    return [x, y]