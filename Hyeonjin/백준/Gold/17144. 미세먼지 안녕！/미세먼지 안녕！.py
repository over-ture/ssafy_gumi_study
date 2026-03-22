# [로직설계]
# 매 초마다 미세먼지 확산 → 공기청정기 작동
# T초 동안 반복한 뒤, 남아있는 미세먼지의 총합을 계산

# 1. 공기청정기 위치 저장

# 2. 시간 반복
# 2-1. 미세먼지 확산 함수
# 모든 칸을 순회하며 미세먼지 확산 수행
#   각 칸의 미세먼지는 `(현재값 // 5)` 만큼 상하좌우로 확산
#   공기청정기 위치에는 확산되지 않음
#   확산된 만큼 기존 위치에서 감소
#   동시에 영향을 반영하기 위해 배열 만들어서 임시로 사용하기


# 2-2. 공기흐름 함수
# 실제 흐름은 오른쪽으로 출발하지만 코드는 반대로 짜야함 (밀어내기) -> AI도움 받음

# 위쪽 공기청정기 (반시계)
#   아래 → 위 → 오른쪽 → 아래 → 왼쪽 순으로 이동
#   순환하면서 먼지를 한 칸씩 밀어냄
#   마지막 공기청정기 옆 칸은 0으로 설정

# 아래쪽 공기청정기 (시계)
#   위 → 아래 → 오른쪽 → 위 → 왼쪽 순으로 이동
#   동일하게 순환 이동
#   마지막 공기청정기 옆 칸은 0으로 설정



import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dust_spread():
    tmp = [[0] * C for _ in range(R)]  # 임시 배열

    for r in range(R):
        for c in range(C):

            if room[r][c] > 0:
                dust = room[r][c] // 5
                counts = 0

                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0 <= nr < R and 0 <= nc < C:
                        if room[nr][nc] != -1:
                            tmp[nr][nc] += dust
                            counts +=1

                room[r][c] -= dust * counts

    for i in range(R):
        for j in range(C):
            room[i][j] += tmp[i][j]
        

def air_flow_up():
    # 위
    for i in range(up-1, 0, -1):
        room[i][0] = room[i-1][0]

    # 오른쪽
    for j in range(C-1):
        room[0][j] = room[0][j+1]
    
    # 아래
    for i in range(up):
        room[i][C-1] = room[i+1][C-1]

    # 왼쪽
    for j in range(C-1, 1, -1):
        room[up][j] = room[up][j-1]

    room[up][1] = 0


def air_flow_down():
    # 아래
    for i in range(down+1, R-1):
        room[i][0] = room[i+1][0]

    # 오른쪽
    for j in range(C-1):
        room[R-1][j] = room[R-1][j+1]

    # 위
    for i in range(R-1, down, -1):
        room[i][C-1] = room[i-1][C-1]

    # 왼쪽
    for j in range(C-1, 1, -1):
        room[down][j] = room[down][j-1]


    room[down][1] = 0

# --------------------------------------------------------

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]


# 공기청정기 r위치
cleaner = []
for i in range(R):
    if room[i][0] == -1:
        cleaner.append(i)

up = cleaner[0]
down = cleaner[1]


# 함수 실행
for i in range(T):
    dust_spread()
    air_flow_up()
    air_flow_down()


# 먼지 개수
total_dust = 0
for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            total_dust += room[i][j]

print(total_dust)