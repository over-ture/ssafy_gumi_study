import sys
input = sys.stdin.readline

# TC = list("".join(input().split())) # 이렇게 하면 두자리수 이상 못 받음
TC = list((input().split()))

King_pos = TC[0] # 킹 초기위치 값
Stone_pos = TC[1] # 돌 초기위치 값

N = int(TC[2])
move = [] # ['B', 'L', 'LB', 'RB', 'LT']
for _ in range(N):
    move.append(input().rstrip())

# 움직임 명령어 딕셔너리
cmd = {
    'R' : (1, 0), 'L' : (-1, 0),
    'B' : (0, -1), 'T' : (0, 1),
    'RT' : (1, 1), 'LT' : (-1, 1),
    'RB' : (1, -1), 'LB' : (-1, -1)
}
# 킹 처음위치 좌표값
Kx = ord(King_pos[0]) - 64
Ky = int(King_pos[1])

# 돌 처음위치 좌표값
Sx = ord(Stone_pos[0]) - 64
Sy = int(Stone_pos[1])

# 체스판 범위
size = 8

# 이제 체스말을 움직여보자
for i in move:
    dx, dy = cmd[i]

    # 한 수 앞의 킹 위치
    will_Kx = Kx + dx
    will_Ky = Ky + dy

    if 1 <= will_Kx <= size and 1 <= will_Ky <= size: # 킹의 예상위치가 체스판 안에 있을 경우

        if will_Kx == Sx and will_Ky == Sy: # 킹의 예상 위치가 현재 돌의 위치와 겹치면
            will_Sx = Sx + dx # 돌의 예상 위치는 킹의 이동범위와 동일
            will_Sy = Sy + dy

            if 1 <= will_Sx <= size and 1 <= will_Sy <= size:
                Kx, Ky = will_Kx, will_Ky # 예상위치로 킹 이동
                Sx, Sy = will_Sx, will_Sy # 예상위치로 돌 이동
            else: # 돌이 나가면 무효
                continue

        else:   # 킹의 예상 위치가 현재 돌의 위치와 안겹치면
            Kx, Ky = will_Kx, will_Ky # 킹만 이동

    else: # 킹이 나가면 무효
        continue

print(chr(Kx + 64) + str(Ky), chr(Sx + 64) + str(Sy), sep = '\n')