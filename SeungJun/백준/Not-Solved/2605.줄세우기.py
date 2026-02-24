# 2605. 줄세우기
T = int(input()) # 학생 수
numbers = list(map(int, input().split()))
student_list = []

for i in range(T) : # 2번 학생부터
    choose_number = numbers[i]
    student_list.insert(i - choose_number, i+1)

print(*student_list)

