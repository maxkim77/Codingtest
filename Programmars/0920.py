#문자열 섞기
#문제 설명
#길이가 같은 두 문자열 str1과 str2가 주어집니다.
#두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.

#제한사항
#1 ≤ str1의 길이 = str2의 길이 ≤ 10
#str1과 str2는 알파벳 소문자로 이루어진 문자열입니다.
#str1	     str2	     result
#"aaaaa"	"bbbbb"	"ababababab"

def solution(str1, str2):
    result = ''
    for i in range(len(str1)): #len은 문자열 str의 길이를 반환합니다.
      result += str1[i] + str2[i]
    return result


#문자열 곱하기

#문제 설명
#문자열 my_string과 정수 k가 주어질 때, my_string을 k번 반복한 문자열을 return 하는 solution 함수를 작성해 주세요.

#제한사항
#1 ≤ my_string의 길이 ≤ 100
#my_string은 영소문자로만 이루어져 있습니다.
#1 ≤ k ≤ 100
#입출력 예
#my_string	k	result
#"string"	3	"stringstringstring"
#"love"	10	"lovelovelovelovelovelovelovelovelovelove"

def solution(my_string, k):
    answer = my_string * k
    return answer
