import math
class Solution(object):
    def isPalindrome(self, s):
        filtered_text = ""
        for ch in s:
            if ch.isalpha():
                filtered_text += ch.lower()

        n = int(math.ceil(len(filtered_text) / 2)) # math.ceil(float): 소수점에 대해 올림 계산, 홀수 처리 위함
        ispalindrome = True
        for i in range(n):
            if filtered_text[i] != filtered_text[len(filtered_text)-i-1]:
                ispalindrome = False # 팰린드롬수가 아닌 것으로 판명 났을 때, 플래그 값을 false로 변경 후, 즉시 탈출
                break

        return ispalindrome
        
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome("race a car"))
print(sol.isPalindrome(" "))
        
# 풀이 
# 글자수 길이의 절반 만큼 실행해서, 앞의 글자와 글자수에서 현재 인덱스 i에 -1를 뺀 인덱스에 접근해서 비교
# 더 빨리(?) for문을 돌고 싶어서 이 로직으로 풀었다. 
