def solution(n):
    composite_count = 0
    for i in range(4, n+1):  # 1, 2, 3은 합성수가 아니므로 4부터 시작
        divisor_count = 0
        for j in range(1, i+1):
            if i % j == 0:
                divisor_count += 1
        if divisor_count >= 3:
            composite_count += 1
    return composite_count