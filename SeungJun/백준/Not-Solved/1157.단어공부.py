def solution(arg) :
    char_list = [] # 중복 없는 글자 수 배치를 위한 리스트
    char_number_list = [] # 각 글자별 횟수를 입력하기 위한 리스트(char_list와 인덱스 순서 일치함)
    arg = arg.upper() # 입력값 대문자화
    for i in arg : # 입력값 글자별로 쪼개서 순회
        if i not in char_list : # 기존에 입력된 글자가 아니면
            char_list.append(i) # 리스트에 추가하고
            char_number_list.append(1) # char_number_list 리스트에 같은 인덱스로 1 추가
        else : # 이미 있는 글자면
            char_number_list[char_list.index(i)] += 1 # 해당 글자와 일치하는 char_number_list 인덱스에 1 추가(출현 횟수 추가)
    
    max_val = max(char_number_list) # 숫자 중 최댓값 구함
    max_char_index = char_list[char_number_list.index(max_val)] # 최댓값에 해당하는 글자 인덱스 찾기
    max_elements = [x for x in char_number_list if x == max_val] # 여러개인지 확인하기 위해 최댓값과 같은 출현 횟수를 갖는 글자 종합
    if len(max_elements) > 1 : # 만약 최댓값 글자가 여러개라면?
        return '?' # ? 출력
    else : 
        return max_char_index # 아니면 최댓값 글자 출력
    
Q = input()
print(solution(Q))