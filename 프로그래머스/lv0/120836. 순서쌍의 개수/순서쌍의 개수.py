def solution(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):  # n의 제곱근까지만 반복
        if n % i == 0:  # i가 n의 약수일 경우
            count += 2  # i와 n/i 두 개의 순서쌍이 생깁니다.
            if i == n // i:  # 만약 n이 제곱수일 경우 중복된 순서쌍을 제거
                count -= 1
    return count
