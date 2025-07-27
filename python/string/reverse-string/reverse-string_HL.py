def reversestring(self, s:List[str]) -> None: #self:클래스 안에서 쓰는 함수, -> None:리스트 안에서 자리만 바꿈
    left, right = 0, len(s) -1 #len(s) -1은 맨 뒤를 가리킴
    while left < right:
        s[left], s[right] = s[right], s[left] #맨 앞과 맨 뒤를 바꿔치기함
        left += 1
        right -= 1 

#reverse() 함수를 쓰는 게 더 간편하지만 공부를 위해 투 포인터를 사용한 코드로 작성해봄        