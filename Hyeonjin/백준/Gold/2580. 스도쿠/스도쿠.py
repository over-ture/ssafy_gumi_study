# [로직설계]
# 1. zeros 리스트에 0의 좌표들을 다 담는다.

# 2. 유효성검사 함수
# 2-1. 가로, 세로 체크
# 2-2. 3*3 박스 체크

# 3. backtracking
# 3-1. idx == len(zeros)라면 스도쿠 판 전체 출력 후 종료.
# 3-2. 1부터 9까지 반복문:
# 3-2-1. check(r, c, num)이 True이면:
# 3-2-1-1. board[r][c] = num
# 3-2-1-2. dfs(idx + 1) 호출
# 3-2-1-3. board[r][c] = 0 (백트래킹)

import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]

# 1. 0의 좌표들
zeros = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zeros.append((i, j))


# 2. 유효성 검사 함수
def check(r, c, num):
    # 2-1. 가로, 세로 체크
    for i in range(9):
        if board[r][i] == num or board[i][c] == num:
            return False
    
    # 2-2. 3*3 박스 체크
    # 현재 좌표가 속한 3*3 박스의 시작점
    start_r, start_c = (r // 3) * 3, (c // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_r + i][start_c + j] == num:
                return False
                
    return True

# 3. backtracking
def dfs(idx):

    # 3-1. 종료조건
    if idx == len(zeros):
        for row in board:
            print(*row)
        exit()
            
    r, c = zeros[idx]

    # 3-2. fill
    for num in range(1, 10):
        if check(r, c, num):
            board[r][c] = num
            dfs(idx + 1)
            board[r][c] = 0

dfs(0)