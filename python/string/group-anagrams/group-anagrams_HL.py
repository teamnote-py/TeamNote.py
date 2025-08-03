import ast
from collections import defaultdict

def group_anagrams(strs):
    anagram_map = defaultdict(list)
    for word in strs:
        key = ''.join(sorted(word))
        anagram_map[key].append(word)
    return list(anagram_map.values())

input_str = input("")  

words = ast.literal_eval(input_str)  # 문자열 → 리스트 변환

result = group_anagrams(words)
print(result)
