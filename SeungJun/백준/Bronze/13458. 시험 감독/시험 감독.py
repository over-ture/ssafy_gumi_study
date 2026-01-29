def solution(a, b, c) :
    left_students = a - b #총감독 1명분만큼 제거

    c_num = left_students // c #부감독관 수는 (남은 학생 수 / c)의 몫 + 1(나머지만큼 1명 더 부감독관 필요)
    if left_students % c != 0 :
        c_num += 1
    result = 1 + c_num # 총감독 1명 + 부감독(남은 부감독 1명 포함)

    if a - b <= 0 : # 총감독 1명이 감당 가능한 경우
        result = 1

    return result

N = int(input())
rooms = list(map(int, input().split()))
main_d, sub_d = map(int, input().split())

total = 0
for i in rooms :
    total += solution(i, main_d, sub_d)

print(total)