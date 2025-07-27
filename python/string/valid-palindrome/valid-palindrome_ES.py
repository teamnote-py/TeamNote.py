#1. 주어진 문자열이 펠린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

strs=[]
a=list(input())
for i in a:
    if i.isalnum():#영문자, 숫자여부 판별
        strs.append(i.lower())
reverse_strs=list(reversed(strs))#reversed 처리만 하면 list가 아니라 인덱싱 불가.

count=0
for i in range(len(strs)):
    if strs[i]!=reverse_strs[i]:
        count+=1
if count==0:
    print("true")
else:
    print("false")

#풀이 결과
# 이 책 자체에서는 함수로 풀이하기 때문에, 추후에 함수로 풀이해야겠다고 느꼈다
# 찾아보니 리트코드 기본양식 - 이미 함수 형태로 주는 양식이기 때문에, body만 구현하면 된다. (추후 리트코드로 수정 및 추가 예정)

#리트코드 방식으로 재풀이 및 채점
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs=[]
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        rev=list(reversed(strs))
        if rev==strs:
            return True
        else:
            return False
#걸린 시간이 11ms로 하위에 속하는 편인 것 같다.
#내가 풀이한 방식 말고 추후 다른 방식을 이용해 시간을 단축시켜야겠다.