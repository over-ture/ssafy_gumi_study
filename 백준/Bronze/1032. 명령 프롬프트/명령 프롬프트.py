T = int(input())
inputs = [] # 입력값 리스트 설정

for i in range(T) :
    inputs.append(input())

file = inputs[0] #초기값 설정(추후 for문 비교를 위함)
file_len = len(inputs[0]) # 파일 길이 설정(모두 같으므로 미리 상수로 정해둠)
result = list(file) # 초기값 설정(1번 입력문으로)

for i in range(len(inputs) - 1) :
    for j in range(file_len) :
        if inputs[i][j] != inputs[i+1][j] : # i번째 입력문의 j번째 글자가 i+1번째 입력문의 j번째 글자와 다르면 
            result[j] = '?'

result = "".join(result)
print(result)