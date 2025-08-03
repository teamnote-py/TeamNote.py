#1. 주어진 문자열이 펠린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

#김혜린----------
def is_palindrome_string(s):
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1:
        if strs.pop(0) != strs.pop(-1): #리스트 맨 앞과 맨 뒤 요소 비교
            return False
    return True

# 입력받아서 결과 출력
input_str = input()
print(is_palindrome_string(input_str))

#풀이 결과
#처음에 while문에 함수가 필요한지 모르고 풀었다가 틀렸다.
#책에서는 함수 선언을 어렵게 해놓아서 쉽게 새로 작성하였다.
#책에 나와있는 데크 자료형과 슬라이싱 사용도 익혀봐야겠다.