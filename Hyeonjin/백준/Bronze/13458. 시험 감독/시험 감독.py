N = int(input())

A = list(map(int, input().split()))

B, C = map(int, input().split())

total = 0 # 일단 감독관 총 수 0으로 지정해놓고..
# 각 시험장 하나씩
for i in A:
    total += 1 # 시험장 개수만큼 총감독관 1명씩 추가
    remain = i - B # 총 감독관이 맡은 학생만큼 응시자에서 빼기

    if remain > 0:
        sub = remain // C # 부감독관 감시가능한 학생을 나눈 몫만큼 부감독관 필요

        if remain % C != 0:
            sub += 1 # 그래도 남은 학생이 있으면 부감독관 1명 추가

        total += sub # total에 부감독관 수 추가

print(total)