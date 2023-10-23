def solution(lines):
    points = []
    for line in lines:
        points.append((line[0], 1))
        points.append((line[1], -1))
        
    points.sort(key=lambda x : x[0])
    
    overlap_length = 0
    line_count = 0
    prev_point = None
    
    for point, delta in points:
        if line_count >= 2 and prev_point is not None:
            #겹치는 구간의 길이를 누적하여 합산합니다.
            overlap_length += point - prev_point
        #선분의 개수를 업데이트합니다.
        line_count += delta
        #이전의 점의 좌표를 업데이트합니다.
        prev_point = point
    return overlap_length