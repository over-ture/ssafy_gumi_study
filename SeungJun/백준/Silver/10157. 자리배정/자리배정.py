c, r = map(int, input().split()) # 가로 0~c-1, 세로 0~r-1인 격자
arr = [[0] * c for _ in range(r)]
k = int(input())
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 북-동-남-서
d = 0
x, y = 0, 0
arr[y][x] = 1
for i in range(2, c*r+1) :
    nx, ny = x + dxs[d], y + dys[d]
    if 0 <= nx < c and 0 <= ny < r and arr[ny][nx] == 0:
        # 가려는 칸이 격자 안에 있고, 빈 칸이라면
        x, y = nx, ny # 이동
    else: # 방향 전환 후 다음 칸으로 이동
        d = (d+1) % 4 # 0->1->2->3->0
        nx, ny = x + dxs[d], y + dys[d]
        x, y = nx, ny
    arr[y][x] = i # 번호 입력
# 좌석배정 완료
# k 좌석 탐색
def find_seat(arr, r, c):
    flag = False
    for i in range(r):
        for j in range(c):
            if arr[i][j] == k:
                flag = True
                print(j+1, i+1)
                return
    if flag == False:
        print(0)
find_seat(arr, r, c)