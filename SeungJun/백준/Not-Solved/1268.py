# 2차원 배열 만들고 각 학년별로 같은 반인 학생 카운트
# 1번씩 걸릴 때마다 같은 반인 학생들의 카운트 +1

N = int(input()) # 학생 수
student_class = [] # 학생 반 2차원 배열(학생, 학년별 반)

for i in range(N) :
    class_input = list(map(int, input().split())) # 특정 학생의 반 입력받음(리스트)
    student_class.append(class_input) # 배열에 추가
    
same = 0
same_class = [] # 각 학생별로 같은 반이었던 수의 배열
# 여기서부터 시작
for class_num in student_class : # 전체 학생 중 n번째 학생에 대하여(특정 학생의 학년 리스트 호출)
    for j in range(N) : # 전체 학생 수만큼 반복
        for k in range(5): # 1~5학년 비교 반복
            if class_num[k] == student_class[j][k] : #특정 학생의 k학년을 다른 학생들의 k학년과 비교
                same += 1
            
    same_class.append(same)
    same = 0

print(same_class)