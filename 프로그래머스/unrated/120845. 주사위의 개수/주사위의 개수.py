def solution(box, n):
    width_dices = box[0] // n
    height_dices = box[1] // n
    depth_dices = box[2] // n
    
    return width_dices * height_dices * depth_dices