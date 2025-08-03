import re
from collections import Counter

def most_common_word(text, banned):
    banned = set(banned)
    words = [w for w in re.sub(r'[^\w\s]', ' ', text.lower()).split() if w not in banned]
    counter = Counter(words)
    return counter.most_common(1)[0][0] if counter else None

# text 입력받기
text = input("")

# banned 단어 리스트 입력받기 (예: hit,ball)
banned_input = input("")
banned = [w.strip() for w in banned_input.split(",") if w.strip()]

result = most_common_word(text, banned)
print(result)
