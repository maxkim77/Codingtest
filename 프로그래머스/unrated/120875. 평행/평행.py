def solution(dots):
    #기울기를 계산하는 함수
    def get_slope(p1, p2):
        return (p2[1] - p1[1]) / (p2[0] - p1[0])
    
    #두 선분이 동일한지 확인하는 함수
    def is_same_line(p1, p2, p3, p4):
        return (p2[1] - p1[1]) * (p4[0] - p3[0]) == (p4[1] - p3[1]) * (p2[0] - p1[0])
    
    for i in range(3):
        for j in range(i+1, 4):
            for k in range(4):
                for l in range(k + 1, 4):
                    if i != k and i != l and j != k and j != l:
                        #기울기 비교
                        if abs(get_slope(dots[i], dots[j]) - get_slope(dots[k], dots[l])) < 1e-9:
                            return 1
                        #두선분이 동일한지 확인
                        if is_same_line(dots[i], dots[j], dots[k], dots[l]):
                            return 1
    return 0