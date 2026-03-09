import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

dxs, dys = [-1, 1, 1, -1], [1, 1, -1, -1] # 대각선 4방향
def in_range(x,y):
    return 0 <= x < N and 0 <= y < N
def search(curr, turn, dir, ate):
    global start
    x, y = curr[0], curr[1]
    if turn == 3:
        if (x, y) == start:
            return len(ate)
        nx, ny = x + dxs[dir], y + dys[dir]
        if in_range(nx, ny) and not vis[nx][ny]:
            if arr[nx][ny] not in ate:
                vis[nx][ny] = True
                ate.append(arr[nx][ny])
                search((nx,ny), turn+1, dir, ate)
                ate.remove(arr[nx][ny])
                vis[nx][ny] = False
    for d in range(4):
        nx, ny = x + dxs[d], y + dys[d]
        if in_range(nx, ny) and not vis[nx][ny]:
            if arr[nx][ny] not in ate:
                vis[nx][ny] = True
                ate.append(arr[nx][ny])
                search((nx,ny), turn+1, d, ate)
                ate.remove(arr[nx][ny])
                vis[nx][ny] = False

    return len(ate)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    vis = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            start = (i,j)
            print(search((i,j),0,0,[]))