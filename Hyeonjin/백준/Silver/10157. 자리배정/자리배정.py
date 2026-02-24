C, R = map(int, input().split())
K = int(input())

grid = []
for i in range(R):
    grid.append([0] * C)

# 델타탐색 4방향 거리 지정
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# 델타탐색 방향 변환
dir_num = [0, 1, 2, 3]
input_dir = 0

# 초기값 설정
r, c = 0, 0
grid[r][c] = 1
number = 2

# 받은 번호표가 총 자리 개수보다 많으면 0출력
if K > R * C:
    print(0)
    exit()

else:
    for i in range(R*C*2):
        cur_dir = input_dir % 4     # 방향 변환 벡터 설정
        nr = r + dr[cur_dir]
        nc = c + dc[cur_dir]
        if grid[r][c] == K:         # 번호표를 찾았으면 좌표 출력 후 종료
            print(c+1, r+1)
            exit()

        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:   # nr, nc 조건설정
            r, c = nr, nc
            grid[r][c] = number
            number += 1
        else:
            input_dir += 1