import sys ; sys.stdin = open('반사경input.txt')

def in_range(x, y):
    global n
    return 0 <= x < n and 0 <= y < n

dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1] # 하 - 상 - 좌 - 우 순서로 배치

def sol(arr):
    d = 3 # 우에서 시작
    x, y = 0, 0
    cnt = 0
    while in_range(x + dxs[d], y + dys[d]):
        nx, ny = x + dxs[d], y + dys[d]
        if in_range(nx, ny) and arr[nx][ny] == 0:
            x, y = nx, ny
        elif arr[nx][ny] == 1:
            d = (d + 2) % 4  # 0<->2, 1<->3,
            cnt += 1
        elif arr[nx][ny] == 2:
            d = 3 - d  # 0<->3, 1<->2
            cnt += 1
        else:
            break
    return cnt

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input().split()))]
    print(f'#{tc} {sol(arr)}')