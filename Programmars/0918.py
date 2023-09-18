#문자열 str이 주어질 때, str을 출력하는 코드를 작성해 보세요.
str = input()  # 사용자에게 입력을 받습니다.
print(str)  # 사용자가 입력한 문자열을 출력합니다.

#a와 b출력하기
a, b = map(int, input().strip().split(' '))

print(f"a = {a}")
print(f"b = {b}\n")

#문자열 반복해서 출력하기
#입력 string 5
#출력 stringstringstringstringstring
a, b = input().strip().split(' ')
b = int(b)
print (a * b)

#대소문자 바꿔서 출력하기
#입력aBcDeFg
#출력AbCdEfG
str = input()
swap_str = str.swapcase()
print(swap_str)

#특수문자 출력하기
#다음과 같이 출력하도록 코드를 작성해 주세요.
#출력 예시: !@#$%^&*(\'"<>?:;

print("!@#$%^&*(\\'\"<>?:;")
