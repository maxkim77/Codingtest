#두 정수 a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요.
#a + b = c
#제한사항
#1 ≤ a, b ≤ 100
#입출력 예
#입력 #1
#4 5
#출력 #1
#4 + 5 = 9

a, b = map(int, input().strip().split(' '))
print(f'{a} + {b} = {a + b}')
  

#문자열 붙여서 출력하기
#문제 설명
#두 개의 문자열 str1, str2가 공백으로 구분되어 입력으로 주어집니다.
#입출력 예와 같이 str1과 str2을 이어서 출력하는 코드를 작성해 보세요.
#제한사항
#1 ≤ str1, str2의 길이 ≤ 10
#입력
#apple pen
#출력
#applepen

str1, str2 = input().strip().split(' ')
print(str1 + str2)


#제한사항
#1 ≤ str의 길이 ≤ 10

#입력 #1
#abcde
#출력 
#a
#b
#c
#d
#e
str = input().strip()

if 1 <= len(str) <= 10:
    for c in str:
        print(c)

#홀짝 구분하기
#문제 설명
#자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 "n is even"을, 홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.

#제한사항
#1 ≤ n ≤ 1,000
#입력 #1
#100
출력 #1
#100 is even
#입력
#1
#출력 #2
#1 is odd
n = int(input().strip())

if 1 <= n <= 1000:
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

#문자열 겹쳐쓰기

#문자열 my_string, overwrite_string과 정수 s가 주어집니다. 문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을 문자열 overwrite_string으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.
#my_string	overwrite_string	s	result
#"He11oWor1d"	"lloWorl"	2	"HelloWorld"
#"Program29b8UYP"	"merS123"	7	"ProgrammerS123"

def solution(my_string, overwrite_string, s):
    # my_string의 시작부터 s까지 + overwrite_string + s 이후부터 my_string의 끝까지
    return my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]

# 테스트 케이스
print(solution("He11oWor1d", "lloWorl", 2))  # "HelloWorld"
print(solution("Program29b8UYP", "merS123", 7))  # "ProgrammerS123"




