num = int(input())
for seq in range(1,num+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    dx = 0
    dy = 1
    x = 0
    y = 0
    cnt = 0
    while 0<=x<n and 0<=y<n:
        nx = x +dx
        ny = y +dy
        if 0<= nx <n and 0<=ny<n:
            if arr[nx][ny] == 1:
                    dx, dy = -dy,-dx
                    cnt += 1
            elif arr[nx][ny] ==2:
                    dx, dy = dy, dx
                    cnt +=1
            x = nx
            y = ny
        else:
            break
    print(f'#{seq} {cnt}')

