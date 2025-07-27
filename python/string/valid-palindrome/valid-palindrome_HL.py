#1. 주어진 문자열이 펠린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

#최은수----------
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
