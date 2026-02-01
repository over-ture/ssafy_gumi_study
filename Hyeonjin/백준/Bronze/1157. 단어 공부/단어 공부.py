S = input()

# 대소문자 구분 안하니 다 대문자로 변환
word = S.upper()

# 아스키코드 A = 65

num_alphabet = [0] * 26 # 알파벳 초기설정 모두 0

for i in word:
    num_alphabet[ord(i) - ord('A')] += 1 # 알파벳 아스키 코드 사용해서 1 ~ 26 숫자 지정

many_count = max(num_alphabet) # 가장 많이 나온 알파벳 숫자로 

if num_alphabet.count(many_count) > 1: # 가장 많이 나온 알파벳 중복되면 ? 출력
    print('?')
else:
    max_index = num_alphabet.index(many_count) # 최댓값 num_alphabet에서 index
    print(chr(max_index + ord('A'))) # 아스키 코드 다시 문자로 변환해서 출력