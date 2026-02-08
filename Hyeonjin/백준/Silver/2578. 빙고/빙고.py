import sys
input = sys.stdin.readline

################################################

def bingo_count(bingo): # 빙고줄 체크하는 함수... 아 디게 머리 아프네
    line = 0

# 가로 빙고 체크
    for i in range(5):
        if sum(bingo[i]) == 0: # i행의 모든 숫자 더했을 때 0이라면
            line += 1 # 빙고줄 1줄 추가

# 세로 빙고 체크
    for i in range(5):
        vertical = 0 # 세로 값 초기설정
        for j in range(5):
                vertical += bingo[j][i] # 세로의 값 다 더했을 때 -> j, i 안바꿔서 틀림;;
        if vertical == 0: # 0이라면
            line += 1 # 빙고줄 1줄 추가

# 왼쪽 위에서 오른쪽 아래로 가는 빙고 체크
    slash1 = 0 # 대각선 위치의 값 초기설정
    for i in range(5):
        slash1 += bingo[i][i] # 대각선 위치의 값을 다 더했을 때
    if slash1 == 0: # 0이라면
        line += 1 # 빙고줄 1줄 추가

# 오른쪽 위에서 왼쪽 아래로 가는 빙고 체크
    slash2 = 0 # 대각선 위치의 값 초기설정
    for i in range(5):
        slash2 += bingo[i][4-i] # 대각선 위치의 값을 다 더했을 때
    if slash2 == 0: # 0이라면
        line += 1 # 빙고줄 1줄 추가

    return line

####################################################

# 철수 빙고판
cheolsoo = []
for i in range(5):
    C = list(map(int, input().split()))
    cheolsoo.append(C)

#################################################

# 사회자가 부르는 빙고 숫자 순서 리스트
answer = []
for i in range(5): # 얘는 검색해야하니까 펼쳐야됨
    A = list(map(int, input().split()))
    for j in A:
        answer.append(j)

##################################################


cnt = 0 # 사회자가 숫자를 부르는 횟수
for num in answer:
    cnt += 1 # 일단 한 번 세고

    for i in range(5):
        for j in range(5):
            if cheolsoo[i][j] == num: # 사회자가 부르는 숫자를
                cheolsoo[i][j] = 0 # 철수의 빙고판에서 0으로 처리

# 빙고줄 3줄 이상이면 끝
    if bingo_count(cheolsoo) >= 3:
        print(cnt)
        exit()