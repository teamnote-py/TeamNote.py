def reorderLogFiles(self, logs: List[str]) -> List[str]:
    letters, digits = [], [] #문자 로그, 숫자 로그 리스트 생성
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log) #숫자 로그 digits에 넣음
        else:
            letters.append(log) #문자 로그 letters에 넣음

    def key(x):
        return (x.split()[1:], x.split()[0]) #내용과 식별자 정렬

    letters.sort(key=key) #내용 기준으로 먼저 정렬, 내용이 같으면 식별자 기준으로 정렬

    return letters + digits #문자 로그+ 숫자 로그

#def말고 람다를 이용하는 게 더 간편한 코드인 것 같음
