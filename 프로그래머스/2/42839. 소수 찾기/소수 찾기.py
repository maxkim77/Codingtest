from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = set()  # 중복된 숫자를 제거하기 위해 set을 사용합니다.

    # 가능한 모든 숫자 조합을 생성합니다.
    for i in range(1, len(numbers) + 1):
        permuted_numbers = permutations(numbers, i)
        for p in permuted_numbers:
            num = int(''.join(p))
            if is_prime(num):
                answer.add(num)

    return len(answer)

# 테스트 예시
print(solution("17"))  # 3
print(solution("011"))  # 2
