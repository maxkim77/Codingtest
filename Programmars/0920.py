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


#문자 리스트를 문자열로 변환하기
#문제 설명
#문자들이 담겨있는 배열 arr가 주어집니다. arr의 원소들을 순서대로 이어 붙인 문자열을 return 하는 solution함수를 작성해 주세요.

#제한사항
#1 ≤ arr의 길이 ≤ 200
#arr의 원소는 전부 알파벳 소문자로 이루어진 길이가 1인 문자열입니다.
#입출력 예
#arr	result
#["a","b","c"]	#"abc"

def solution(arr):
    return ''.join(arr)

arr = ["a", "b", "c"]
print(solution(arr))

#문자열 곱하기
#문제 설명
#문자열 my_string과 정수 k가 주어질 때, my_string을 k번 반복한 문자열을 return 하는 solution 함수를 작성해 주세요.

def solution(my_string, k):
    answer = my_string * k
    return answer
    
#문제 설명
#연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.

#12 ⊕ 3 = 123
#3 ⊕ 12 = 312
#양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.
#단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.
#제한사항
#1 ≤ a, b < 10,000
#입출력 예
#a	b	result
#9	91	991
#89	8	898

def solution(a, b):
    concat_ab = int(str(a)+str(b))
    concat_ba = int(str(b)+str(a))
    answer = max(concat_ab, concat_ba)
    return answer
