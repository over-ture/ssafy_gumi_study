num = int(input())
for tc in range(1,num+1):
    n = int(input())
    visited = [[0] * n for _ in range(n)]
    arr = [list(map(int,input())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j]==2:
                start = (i,j)
    stack = [start]
    visited[start[0]][start[1]] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = 0
    while stack:
        x,y = stack[-1]

        if arr[x][y] ==3:
            result = 1
            break
        moved = False
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny] !=1 and visited[nx][ny]==0:
                    stack.append((nx,ny))
                    visited[nx][ny]= 1
                    moved = True
                    break
        if not moved:
            stack.pop()

    print(f'#{tc} {result}')