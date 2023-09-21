#n의 배수
#문제 설명
#정수 num과 n이 매개 변수로 주어질 때, num이 n의 배수이면 1을 return n의 배수가 아니라면 0을 return하도록 solution 함수를 완성해주세요.
def solution(num, n):
    answer = 1 if num % n == 0 else 0
    return answer
#문제 설명
#정수 number와 n, m이 주어집니다. number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.
def solution(number, n, m):
    answer = 1 if number % n == 0 and number % m == 0 else 0
    return answer

#홀짝에 따라 다른 값 반환하기
#문제 설명
#양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.
def solution(n):
    if n % 2 == 1:
        answer = sum(i for i in range(1,n+1) if i % 2 == 1)
    else:
        answer = sum(i**2 for i in range(2,n+1,2))
    return answer
