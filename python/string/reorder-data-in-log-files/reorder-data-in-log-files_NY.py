class Solution(object):
    def reorderLogFiles(self, logs):
        digits = []
        letters = []

        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)


        letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
        

# 일단 문제도 이해 안가고 람다 표현식을 몰랐고 또 split도 구면이기 때문에 너무 헤맸다능...
# 모든 log는 "식별자 + (숫자 또는 문자)""로 이루어지는데

# 1. 우선 문자로 이루어진 letters 과 숫자로 이루어진 digits를 따로 저장한뒤
# 2. 문자로 이루어져있는 log를 저장한 배열인 letters에 람다함수를 써준다. 이때의 정렬 기준은..
#  a. log를 공백기준으로 다 split해서 식별자 이후인 [1:] 1번째 인덱스부터
#  b. 만약 log 내용이 같다면 후순위 기준인 식별자 [0] 를 기준으로 정렬
# 3. digits 는 배열의 상대적인 순서를 기준으로 하므로 사전순이나 어떤 규칙없이 따로 정렬 안해줘도 되니까 패스
# 4. 문제의 조건인 letters -> digits 순에의해서 그냥 letters + digits를 return 해주면된다.

# 이거는 문제가 좀 어려웠당