class Solution:
    def reverseString(self, s: List[str]) -> None:
        rev=[]
        for i in range(len(s)-1,-1,-1):
            rev.append(s[i])
        s[:]=rev

# => 더 단축해서 작성 (슬라이싱 이용)
# s = rev -> 이런식으로 하면 포인터만 이동된다. (함수 내부의 참조만 바뀜.)
# but s[:] = rev -> s리스트 내부 데이터 자체를 덮어씀.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:]=s[::-1]
#이건 코드 길이 단축. but 메모리를 더 잡아먹는다.